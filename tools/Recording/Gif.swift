// Turns a screen recording into an animated GIF with the system's own frameworks, or samples frames from it as PNG.
//
//   swift tools/Recording/Gif.swift gif <movie> <gif> <frames per second> <width>
//   swift tools/Recording/Gif.swift frames <movie> <directory> <second>...

import AVFoundation
import CoreGraphics
import Foundation
import ImageIO
import UniformTypeIdentifiers

func image(_ generator: AVAssetImageGenerator, at seconds: Double) -> CGImage? {
    try? generator.copyCGImage(at: CMTime(seconds: seconds, preferredTimescale: 600), actualTime: nil)
}

func scaled(_ source: CGImage, width: Int) -> (CGImage, Data)? {
    let height = Int(Double(source.height) * Double(width) / Double(source.width))
    guard let context = CGContext(data: nil, width: width, height: height, bitsPerComponent: 8, bytesPerRow: width * 4, space: CGColorSpaceCreateDeviceRGB(), bitmapInfo: CGImageAlphaInfo.noneSkipLast.rawValue) else { return nil }
    context.interpolationQuality = .high
    context.draw(source, in: CGRect(x: 0, y: 0, width: width, height: height))
    guard let result = context.makeImage(), let bytes = context.data else { return nil }
    return (result, Data(bytes: bytes, count: width * height * 4))
}

func generator(for path: String) -> (AVAssetImageGenerator, Double) {
    let asset = AVURLAsset(url: URL(fileURLWithPath: path))
    let made = AVAssetImageGenerator(asset: asset)
    made.requestedTimeToleranceBefore = .zero
    made.requestedTimeToleranceAfter = .zero
    return (made, CMTimeGetSeconds(asset.duration))
}

func gif(movie: String, output: String, fps: Double, width: Int) -> Int32 {
    let (frames, duration) = generator(for: movie)
    var kept: [(CGImage, Double)] = []
    var previous: Data?
    var second = 0.0

    while second < duration {
        if let source = image(frames, at: second), let (frame, bytes) = scaled(source, width: width) {
            if bytes == previous, let last = kept.popLast() {
                kept.append((last.0, last.1 + 1 / fps))
            } else {
                kept.append((frame, 1 / fps))
                previous = bytes
            }
        }

        second += 1 / fps
    }

    guard let destination = CGImageDestinationCreateWithURL(URL(fileURLWithPath: output) as CFURL, UTType.gif.identifier as CFString, kept.count, nil) else { return 1 }
    CGImageDestinationSetProperties(destination, [kCGImagePropertyGIFDictionary: [kCGImagePropertyGIFLoopCount: 0]] as CFDictionary)

    for (frame, delay) in kept {
        CGImageDestinationAddImage(destination, frame, [kCGImagePropertyGIFDictionary: [kCGImagePropertyGIFUnclampedDelayTime: delay, kCGImagePropertyGIFDelayTime: delay]] as CFDictionary)
    }

    print("\(kept.count) distinct frames over \(String(format: "%.1f", duration)) s")
    return CGImageDestinationFinalize(destination) ? 0 : 1
}

func frames(movie: String, directory: String, seconds: [Double]) -> Int32 {
    let (frames, _) = generator(for: movie)

    for second in seconds {
        guard let source = image(frames, at: second), let destination = CGImageDestinationCreateWithURL(URL(fileURLWithPath: "\(directory)/frame-\(second).png") as CFURL, UTType.png.identifier as CFString, 1, nil) else { return 1 }
        CGImageDestinationAddImage(destination, source, nil)
        CGImageDestinationFinalize(destination)
    }

    return 0
}

let arguments = CommandLine.arguments

if arguments.count >= 6, arguments[1] == "gif" {
    exit(gif(movie: arguments[2], output: arguments[3], fps: Double(arguments[4]) ?? 10, width: Int(arguments[5]) ?? 900))
}

if arguments.count >= 5, arguments[1] == "frames" {
    exit(frames(movie: arguments[2], directory: arguments[3], seconds: arguments[4...].compactMap(Double.init)))
}

print("usage: Gif.swift gif <movie> <gif> <fps> <width> | frames <movie> <directory> <second>...")
exit(2)
