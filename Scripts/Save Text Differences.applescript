-- Copyright 2020, Darin Franklin
-- https://github.com/darinfranklin/AutomationForAccordance
on run {}
	-- Save Text Differences to a temp file.
	-- Remove the file first so we are not prompted to replace it.
	set filename to "/tmp/accdiff.txt"
	-- Set the maximum time (in seconds) we want to wait for Accordance to save the file
	set maxDelay to 60
	do shell script "rm -f " & filename
	tell application "Accordance" to activate
	delay 0.5
	tell application "System Events" to tell process "Accordance"
		tell menu bar 1 to tell menu bar item "Display" to tell menu 1 to tell menu item "List Text Differences" to click
		delay 1
		tell menu bar 1 to tell menu bar item "File" to tell menu 1 to tell menu item "Save as Text File" to tell menu 1 to tell menu item "Plain Text…" to click
		tell window "Save" to tell text field "Save As:"
			keystroke filename
			keystroke return
			delay 1
			keystroke return
		end tell
	end tell
	delay 1
	waitForFile(filename, maxDelay)
end run

on waitForFile(filename, sec)
	set pollMax to sec
	set poll to 0
	set waiting to true
	repeat while waiting
		set poll to poll + 1
		tell application "System Events" to set waiting to ((size of file filename) = 0) and poll < pollMax
		if waiting then delay 1
	end repeat
end waitForFile
