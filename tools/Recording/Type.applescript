-- Types a line into the front Terminal window one key at a time, at a person's pace, and stops if Terminal loses focus.
on run argv
  set phrase to item 1 of argv
  tell application "Terminal" to activate
  delay 0.4
  tell application "System Events"
    set frontName to name of (first process whose frontmost is true)
    if frontName is not "Terminal" then return "not-front: " & frontName
    repeat with c in characters of phrase
      set frontName to name of (first process whose frontmost is true)
      if frontName is not "Terminal" then return "lost-focus: " & frontName
      keystroke (c as text)
      delay (0.045 + (random number from 0 to 70) / 1000)
    end repeat
    delay 0.5
    key code 36
  end tell
  return "typed"
end run
