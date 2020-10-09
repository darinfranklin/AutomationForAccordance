-- Open a URL in the Accordance web browser.
-- Run from the command line:
-- osascript accordweb.applescript "https://accordancebible.com/forums"
on run (argv)
	set loc to item 1 of argv
	tell application "Accordance"
		activate
		tell application "System Events" to tell process "Accordance"
			set mFile to 3 -- "File"
			set mNewTab to 1 -- "New Tab"
			set mWebBrowser to 39 -- "Web Browser"
			tell menu bar 1 to tell menu bar item mFile to tell menu 1 to tell menu item mNewTab to tell menu 1 to tell menu item mWebBrowser to click
			key down command
			delay 0.3
			keystroke "l"
			delay 0.3
			key up command
			delay 0.3
			keystroke loc
			keystroke return
		end tell
	end tell
end run
