#!/usr/bin/python
import unittest
from romnum import romNumVal

class TestRomNumVal(unittest.TestCase):
   def test_romNumVal(self):
      self.assertEqual(romNumVal(''), 0)
      self.assertEqual(romNumVal('i'), 1)
      self.assertEqual(romNumVal('ii'), 2)
      self.assertEqual(romNumVal('iii'), 3)
      self.assertEqual(romNumVal('iv'), 4)
      self.assertEqual(romNumVal('v'), 5)
      self.assertEqual(romNumVal('vi'), 6)
      self.assertEqual(romNumVal('vii'), 7)
      self.assertEqual(romNumVal('viii'), 8)
      self.assertEqual(romNumVal('ix'), 9)
      self.assertEqual(romNumVal('x'), 10)
      self.assertEqual(romNumVal('xiv'), 14)
      self.assertEqual(romNumVal('xix'), 19)
      self.assertEqual(romNumVal('xxxi'), 31)
      self.assertEqual(romNumVal('xli'), 41)
      self.assertEqual(romNumVal('liv'), 54)
      self.assertEqual(romNumVal('xciv'), 94)
      self.assertEqual(romNumVal('cc'), 200)
      self.assertEqual(romNumVal('ccclix'), 359)
      self.assertEqual(romNumVal('ccclxxx'), 380)

   def test_romNumValUppecase(self):
      self.assertEqual(romNumVal('CLXIV'), 164)

if __name__ == '__main__':
   suite = unittest.TestLoader().loadTestsFromTestCase(TestRomNumVal)
   unittest.TextTestRunner(verbosity=2).run(suite)
