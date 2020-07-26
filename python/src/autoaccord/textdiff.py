# Read the Text Differences file from Accordance and convert to an accord URL.
# File > Save as Text File > Plain Text...
import sys
import io
import re
from verses import consolidate, accordURL

def extractTextName(header):
   m = re.match(r'(.*?)\s*\t(.*?)\t(.*)', header, flags=re.U)
   return m.group(2) if m != None else ''      

def extractVerses(lines):
   #lines = re.sub(r'.*\[.*', '', lines, flags=re.U) # remove lines with bracketed text
   lines = re.sub(r'\s*\t.*', '', lines, flags=re.U) # remove column 2 and 3
   lines = re.sub(r'\n+', ';', lines, flags=re.U)    # join all with ;
   lines = re.sub(r'^;|;$', '', lines, flags=re.U)   # remove leading and trailing ;
   return lines

# Reads /tmp/accdiff.txt
# Extracts the verse references.
# Prints the URL: accord://read/KJVS?Gen 1:1,2,3; Exod 1:1
if __name__ == '__main__':
   fn = sys.argv[1] if len(sys.argv) > 1 else '/tmp/accdiff.txt'
   with io.open(fn, mode='r', encoding='utf_16') as f:
      header = f.readline()
      lines = f.read()
   text = extractTextName(header)
   verses = consolidate(extractVerses(lines))
   print(accordURL(text, verses))
