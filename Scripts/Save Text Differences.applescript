-- Copyright 2020, Darin Franklin
-- https://github.com/darinfranklin/AutomationForAccordance
global mDisplay, mListTextDifferences, mFile, mSaveAsTextFile, mPlainText, mSave, mSaveAs
on run {}
	-- Save Text Differences to a temp file.
	-- Remove the file first so we are not prompted to replace it.
	set filename to "/tmp/accdiff.txt"
	-- Set the maximum time (in seconds) we want to wait for Accordance to save the file
	set maxDelay to 60
	do shell script "rm -f " & filename
	setMenuNames()
	tell application "Accordance" to activate
	delay 0.5
	tell application "System Events" to tell process "Accordance"
		tell menu bar 1 to tell menu bar item mDisplay to tell menu 1 to tell menu item mListTextDifferences to click
		delay 1
		tell menu bar 1 to tell menu bar item mFile to tell menu 1 to tell menu item mSaveAsTextFile to tell menu 1 to tell menu item mPlainText to click
		tell window mSave to tell text field mSaveAs
			keystroke filename
			keystroke return
			delay 1
			keystroke return
		end tell
	end tell
	delay 1
	waitForFile(filename, maxDelay)
end run

on setMenuNames()
	set lang to (characters 1 through 2 of user locale of (system info)) as text
	if (lang = "en") then
		set mDisplay to "Display"
		set mListTextDifferences to "List Text Differences"
		set mFile to "File"
		set mSaveAsTextFile to "Save as Text File"
		set mPlainText to "Plain Text…"
		set mSave to "Save"
		set mSaveAs to "Save As:"
	else if (lang = "de") then
		set mDisplay to "Darstellung"
		set mListTextDifferences to "Unterschiede auflisten"
		set mFile to "Ablage"
		set mSaveAsTextFile to "Als Textdatei sichern"
		set mPlainText to "Reiner Text…"
		set mSave to "Sichern"
		set mSaveAs to "Sichern als:"
	else if (lang = "es") then
		set mDisplay to "Visualizacin"
		set mListTextDifferences to "Mostrar diferencias en los textos"
		set mFile to "Archivo"
		set mSaveAsTextFile to "Guardar como archivo de texto"
		set mPlainText to "Texto sin formato…"
		set mSave to "Guardar"
		set mSaveAs to "Guardar como:"
	else
		-- Try by number, but the Display menu has extra items for "de" and "es". Other languages might also.
		set mDisplay to 6
		--set mListTextDifferences to 11
		set mListTextDifferences to 8
		set mFile to 3
		set mSaveAsTextFile to 20
		set mPlainText to 1
		set mSave to 1
		set mSaveAs to 1
	end if
	
end setMenuNames

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
