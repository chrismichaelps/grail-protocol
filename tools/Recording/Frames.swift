// Encodes captured browser states as a paced walkthrough, with explicit scene labels.
// Usage: swift Frames.swift <manifest.json> <output.mp4> <preview.gif>
import AVFoundation
import CoreGraphics
import CoreText
import Foundation
import ImageIO
import UniformTypeIdentifiers

struct Scene: Decodable {
    let image: String
    let seconds: Double
    let title: String
    let note: String
    let preview: Bool
}

struct Manifest: Decodable {
    let width: Int
    let height: Int
    let scenes: [Scene]
}

enum Failure: Error { case invalidManifest, image, context, buffer, encode }

func frame(_ scene: Scene, base: URL, width: Int, height: Int) throws -> CGImage {
    let url = base.appendingPathComponent(scene.image)
    guard let source = CGImageSourceCreateWithURL(url as CFURL, nil),
          let image = CGImageSourceCreateImageAtIndex(source, 0, nil) else { throw Failure.image }
    guard let context = CGContext(data: nil, width: width, height: height, bitsPerComponent: 8,
                                  bytesPerRow: width * 4, space: CGColorSpaceCreateDeviceRGB(),
                                  bitmapInfo: CGImageAlphaInfo.noneSkipFirst.rawValue) else { throw Failure.context }
    context.setFillColor(CGColor(red: 0.035, green: 0.09, blue: 0.08, alpha: 1))
    context.fill(CGRect(x: 0, y: 0, width: width, height: height))
    let contentHeight = Double(height - 76)
    let scale = min(Double(width) / Double(image.width), contentHeight / Double(image.height))
    let size = CGSize(width: Double(image.width) * scale, height: Double(image.height) * scale)
    context.interpolationQuality = .high
    context.draw(image, in: CGRect(x: (Double(width) - size.width) / 2, y: (contentHeight - size.height) / 2,
                                  width: size.width, height: size.height))
    for (text, fontSize, y) in [(scene.title, 21.0, Double(height - 30)), (scene.note, 13.0, Double(height - 55))] {
        let attributes: [NSAttributedString.Key: Any] = [
            NSAttributedString.Key(kCTFontAttributeName as String): CTFontCreateWithName("Helvetica" as CFString, fontSize, nil),
            NSAttributedString.Key(kCTForegroundColorAttributeName as String): CGColor(gray: 1, alpha: 1)
        ]
        let line = CTLineCreateWithAttributedString(NSAttributedString(string: text, attributes: attributes))
        context.textPosition = CGPoint(x: 22, y: y)
        CTLineDraw(line, context)
    }
    guard let made = context.makeImage() else { throw Failure.image }
    return made
}

func writeMovie(_ manifest: Manifest, base: URL, output: URL) throws {
    let writer = try AVAssetWriter(outputURL: output, fileType: .mp4)
    let temporary = FileManager.default.temporaryDirectory.appendingPathComponent("grail-video-" + UUID().uuidString)
    try FileManager.default.createDirectory(at: temporary, withIntermediateDirectories: true)
    defer { try? FileManager.default.removeItem(at: temporary) }
    writer.directoryForTemporaryFiles = temporary
    writer.shouldOptimizeForNetworkUse = true
    let input = AVAssetWriterInput(mediaType: .video, outputSettings: [
        AVVideoCodecKey: AVVideoCodecType.h264,
        AVVideoWidthKey: manifest.width,
        AVVideoHeightKey: manifest.height,
        AVVideoCompressionPropertiesKey: [AVVideoAverageBitRateKey: 800_000, AVVideoMaxKeyFrameIntervalKey: 25]
    ])
    input.expectsMediaDataInRealTime = false
    let adaptor = AVAssetWriterInputPixelBufferAdaptor(assetWriterInput: input, sourcePixelBufferAttributes: [
        kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32ARGB,
        kCVPixelBufferWidthKey as String: manifest.width,
        kCVPixelBufferHeightKey as String: manifest.height,
        kCVPixelBufferCGImageCompatibilityKey as String: true,
        kCVPixelBufferCGBitmapContextCompatibilityKey as String: true
    ])
    writer.add(input)
    guard writer.startWriting() else { throw writer.error ?? Failure.encode }
    writer.startSession(atSourceTime: .zero)
    var position: Int64 = 0
    for scene in manifest.scenes {
        let image = try frame(scene, base: base, width: manifest.width, height: manifest.height)
        var pixel: CVPixelBuffer?
        guard let pool = adaptor.pixelBufferPool,
              CVPixelBufferPoolCreatePixelBuffer(nil, pool, &pixel) == kCVReturnSuccess,
              let buffer = pixel else { throw Failure.buffer }
        CVPixelBufferLockBaseAddress(buffer, [])
        guard let context = CGContext(data: CVPixelBufferGetBaseAddress(buffer), width: manifest.width,
                                      height: manifest.height, bitsPerComponent: 8,
                                      bytesPerRow: CVPixelBufferGetBytesPerRow(buffer), space: CGColorSpaceCreateDeviceRGB(),
                                      bitmapInfo: CGImageAlphaInfo.noneSkipFirst.rawValue) else { throw Failure.context }
        context.draw(image, in: CGRect(x: 0, y: 0, width: manifest.width, height: manifest.height))
        CVPixelBufferUnlockBaseAddress(buffer, [])
        for _ in 0..<Int((scene.seconds * 5).rounded()) {
            while !input.isReadyForMoreMediaData {
                if writer.status == .failed { throw writer.error ?? Failure.encode }
                Thread.sleep(forTimeInterval: 0.01)
            }
            guard adaptor.append(buffer, withPresentationTime: CMTime(value: position, timescale: 5)) else {
                throw writer.error ?? Failure.encode
            }
            position += 1
        }
    }
    writer.endSession(atSourceTime: CMTime(value: position, timescale: 5))
    input.markAsFinished()
    let done = DispatchSemaphore(value: 0)
    writer.finishWriting { done.signal() }
    done.wait()
    guard writer.status == .completed else { throw writer.error ?? Failure.encode }
}

func writePreview(_ manifest: Manifest, base: URL, output: URL) throws {
    let scenes = manifest.scenes.filter(\.preview)
    guard let destination = CGImageDestinationCreateWithURL(output as CFURL, UTType.gif.identifier as CFString, scenes.count, nil) else { throw Failure.encode }
    CGImageDestinationSetProperties(destination, [kCGImagePropertyGIFDictionary: [kCGImagePropertyGIFLoopCount: 0]] as CFDictionary)
    for scene in scenes {
        let image = try frame(scene, base: base, width: 960, height: (manifest.height * 960 / manifest.width) / 2 * 2)
        CGImageDestinationAddImage(destination, image, [kCGImagePropertyGIFDictionary: [kCGImagePropertyGIFUnclampedDelayTime: 4.0]] as CFDictionary)
    }
    guard CGImageDestinationFinalize(destination) else { throw Failure.encode }
}

let args = CommandLine.arguments
if args.count != 4 { fatalError("usage: Frames.swift <manifest.json> <output.mp4> <preview.gif>") }
let url = URL(fileURLWithPath: args[1])
let manifest = try JSONDecoder().decode(Manifest.self, from: Data(contentsOf: url))
guard manifest.width >= 960, manifest.height > 76, manifest.width % 2 == 0, manifest.height % 2 == 0,
      !manifest.scenes.isEmpty, manifest.scenes.contains(where: \.preview),
      manifest.scenes.allSatisfy({ $0.seconds >= 1 && $0.seconds <= 30 }) else { throw Failure.invalidManifest }
try writeMovie(manifest, base: url.deletingLastPathComponent(), output: URL(fileURLWithPath: args[2]))
try writePreview(manifest, base: url.deletingLastPathComponent(), output: URL(fileURLWithPath: args[3]))
print("Encoded \(manifest.scenes.count) captured states, \(manifest.scenes.reduce(0) { $0 + $1.seconds }) seconds")
