# Automation for Accordance

This project contains scripts and Automator workflows for use with [Accordance Bible Software](https://www.accordancebible.com/) on macOS.

# Services

Find the Automator workflow files under the Services folder in this project.

* Open Text Differences as Search.workflow
* Open Text Differences as Web Page.workflow
* Normalize Verse Search.workflow

Double-click on the workflow files to install them.  They get copied into ~/Library/Services, and they appear in the menu at Accordance > Services > ….

You may have to grant permission to allow the services to run.

You can assign keyboard shortcuts for the services.
Accordance > Services > Service Preferences…


## Text Differences

Accordance has a [Compare Texts](http://accordancefiles2.com/helpfiles/STC/content/topics/04_gswa/compare_texts.htm) feature which marks the differences between two text modules, but it does not have any navigation for the differences.  There is no way to move to the next or previous difference. Accordance also has a List Text Differences report, but it also lacks any navigation or links.

These two Automator workflows provide navigation and links for the text differences.

### Open Text Differences as Search

This service opens a Text Differences tab, saves it, reads it, and then opens the Search tab with the list of verses.

1. In Accordance, open two texts in parallel, enable Compare, and turn on "Recycle Contents".
2. Accordance > Services > Open Text Differences as Search


### Open Text Differences as Web Page

Do the same steps as above, but choose Accordance > Services > Open Text Differences as Web Page.

It creates an HTML file and opens it in the default web browser.  To view this file in Accordance, you have to copy and paste the URL into the Accordance web browser tab (File > New Tab > Web Browser).  There is currently no way for the script to open it directly in Accordance, but I will add that feature if Accordance ever gets a keyboard shortcut to select the URL bar (Cmd-L, perhaps).


## Normalize Verse Search

Sometimes you will find Bible verses in a PDF or web page which use Roman numerals for chapter numbers or have extra punctuation. Accordance search will give an error if the list does not follow its formatting rules. The Normalize Verse Search service cleans up the list of verses into a format that Accordance will accept.

1. Copy and paste a list of verses into the Search tab: i. Chron. i. 13;; ii. Chron. iv. 19;
2. Do not press return yet.
3. Accordance > Services > Normalize Verse Search

It changes the search to: 1Chron 1:13; 2Chron 4:19


# Implementation

The scripts are written in Python, with some AppleScript to control Accordance.

The project contains these directories.

* python    - master copy of the Python code which is in the workflow
* Scripts   - master copy of the AppleScript code which is in the workflow
* Services  - workflows, hand assembled from the master scripts

To build the Automator workflows, I copy the scripts manually and paste them into Automator.  I have to replace all of the import statements with the code that would be imported, since there is no way to package libraries inside a workflow.  An alternative is to install the Python scripts to ~/Library/Python/2.7/lib/python/site-packages, but then the workflow is not self-contained.

## Unit Tests

Unit tests verify that the code works.

```
% cd python
% ./test.sh 
test_romNumVal (test.test_romnum.TestRomNumVal) ... ok
test_romNumValUppecase (test.test_romnum.TestRomNumVal) ... ok
test_accordURL (test.test_accordURL.TestAccordURL) ... ok
test_accordURLEscape (test.test_accordURL.TestAccordURL) ... ok
test_consolidate (test.test_verses.TestVerses) ... ok
test_consolidateBookWithNumber (test.test_verses.TestVerses) ... ok
test_consolidateSameBook (test.test_verses.TestVerses) ... ok
test_consolidateSameChapter (test.test_verses.TestVerses) ... ok
test_normalize (test.test_verses.TestVerses) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.002s

OK
```
