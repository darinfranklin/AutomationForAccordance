# Read the Text Differences file from Accordance and convert to HTML.
# File > Save as Text File > Plain Text...
import sys
import io
import re
from verses import consolidate, accordURL
from textdiff import extractTextName, extractVerses

textName = ''
allVerses = ''

def tagHeaderLine(m):
   global allVerses
   col1 = m.group(1)
   text1 = m.group(2)
   text2 = m.group(3)
   return u'<tr><th>{}</th><th><a href="{}">{}</a></th><th>{}</th></tr>'.format(
      col1, accordURL(text1, allVerses), text1, text2)

def tagHeader(header, verses):
   global allVerses
   allVerses = verses
   header = re.sub(r'(.*?)\s*\t(.*?)\t(.*)', tagHeaderLine, header, flags=re.U)
   return header

def tagVerseLine(m):
   global textName
   verse = m.group(1)
   if len(verse) > 0:
      return u'<tr><th><a href="{}">{}</a></th><td>{}</td><td>{}</td></tr>'.format(
            accordURL(textName, verse), verse, m.group(2), m.group(3))
   else:
      return u'<tr><th>{}</th><td>{}</td><td>{}</td></tr>'.format(
            verse, m.group(2), m.group(3))

def tagVerses(lines, text):
   global textName
   textName = text
   lines = re.sub(r'(.*?)\s*\t(.*?)\t(.*)', tagVerseLine, lines, flags=re.U)
   return lines

def composeHTML(header, lines, text, verses):
   htmlHeader = u"""<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8"/>
      <title>Text Differences</title>
      <style>
         table, th, td {
            padding: 5px;
         }
         th, td {
            text-align: left;
         }
         th {
            font-size: smaller;
            font-family: sans-serif;
            white-space: nowrap;
         }
         td {
            font-size: larger;
            font-family: Accordance, Times New Roman, serif;
         }
      </style>
   </head>
   <body>
      <table>
"""
   htmlTableHeader = tagHeader(header, verses)
   htmlTableRows = tagVerses(lines, text)
   htmlFooter = u'</table></body></html>'
   return htmlHeader + htmlTableHeader + htmlTableRows + htmlFooter

# Reads /tmp/accdiff.txt
# Rewrites the whole file as HTML.
# Prints the URL: file:///tmp/accdiff.html
if __name__ == '__main__':
   fn = sys.argv[1] if len(sys.argv) > 1 else '/tmp/accdiff.txt'
   fnout = '/tmp/accdiff.html'
   with io.open(fn, mode='r', encoding='utf_16') as f:
      header = f.readline()
      lines = f.read()
   text = extractTextName(header)
   verses = consolidate(extractVerses(lines))
   with io.open(fnout, 'w', encoding='utf_8') as f:
      f.write(composeHTML(header, lines, text, verses))
   print('file://{}'.format(fnout))
