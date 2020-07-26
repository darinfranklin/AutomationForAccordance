# Transform Bible verse lists into a format that Accordance accepts.
import re
from romnum import romNumVal
from urllib import quote

def escapePath(value):
   return quote(value.encode('utf_8'))

def escapeQuery(value):
   value = value.replace(' ', '_')
   return quote(value.encode('utf_8'), ':;,._')

def accordURL(text, verses):
   return 'accord://read/{}?{}'.format(escapePath(text), escapeQuery(verses))

# Group book and chapter refs into a shorter form: Gen 1:1; Gen 1:3; Gen 2:1 -> Gen 1:1,3; 2:1
def consolidate(verses):
   result = ''
   curbook = ''
   curchap = 0
   for verse in verses.split(';'):
      verse  = verse.strip()
      sep = '; '
      match = re.search('\s*(.*?)\s+(\d*:?\d+)', verse)
      if match != None:
         book = match.group(1)
         ref = match.group(2)
         match = re.search('(\d+):(\d+)', ref)
         if match != None:
            ch = match.group(1)
            vs = match.group(2)
         else:
            ch = 1
            vs = ref
         if book == curbook:
            verse = ref
            if curchap == ch:
               sep = ','
               verse = vs
            else:
               curchap = ch
         else:
            curbook = book
            curchap = ch
      if result != '':
         result = result + sep
      result = result + verse
   return result

def rn(match):
   return str(romNumVal(match.group(1)))

# Handles Roman numerals and extraneous punctuation.
def normalize(refs):
   refs = re.sub(r'\s+', r' ', refs, re.U)  # combine redundant spaces
   refs = re.sub(r'\s+([,;])', r'\1', refs, re.U) # remove space before punctuation
   refs = re.sub(r'\\u2013', r'-', refs, re.U) # en dash to hyphen
   refs = re.sub(r'\s*-\s*', r'-', refs, re.U) # remove spaces around hyphen
   refs = re.sub(r'\b([clxvi]+)\b', rn, refs, re.U | re.I) # decode Roman numeral
   refs = re.sub(r'(\d+)[.:] *(\d+)', r'\1:\2', refs, re.U) # use : for verses
   refs = re.sub(r'(\w+)\.', r'\1', refs, re.U) # remove . after book number
   refs = re.sub(r'(\d+)\s+([A-Za-z]+)', r'\1\2', refs, re.U) # join book num and name
   refs = re.sub(r'([,;]){2,}', r'\1', refs, re.U) # combine redundant punctuation
   refs = re.sub(r'^[ ,;]+|[ ,;]+$', r'', refs, re.U) # leading/trailing junk
   return refs

if __name__ == '__main__':
   import fileinput
   for line in fileinput.input():
      print(consolidate(normalize(line)))
