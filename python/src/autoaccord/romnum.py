#  Convert Roman numerals to integers.
import re

nums = {'m': 1000, 'd': 500, 'c': 100, 'l': 50, 'x': 10, 'v': 5, 'i': 1}

def valRN(r):
   return nums[r] if r in nums else 0

def romNumVal(rom):
   vals = []
   for rn in rom.lower():
      vals.append(valRN(rn))
   val = 0
   length = len(vals)
   for i in range(0, length):
      v0 = vals[i]
      if (i + 1 < length) and (v0 < vals[i + 1]):
         v0 *= -1
      val += v0
   return val


if __name__ == '__main__':
   import fileinput
   for line in fileinput.input():
      print(romNumVal(line))
