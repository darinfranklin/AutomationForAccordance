#!/usr/bin/python
import unittest
from verses import consolidate, normalize

class TestVerses(unittest.TestCase):
   def test_consolidate(self):
      self.assertEqual(consolidate('John 1:1'), 'John 1:1')

   def test_consolidateSameBook(self):
      self.assertEqual(consolidate('John 1:1; John 2:2'), 'John 1:1; 2:2')
      self.assertEqual(consolidate('John 1:1; John 2:2; Acts 1:2'), 'John 1:1; 2:2; Acts 1:2')
      self.assertEqual(consolidate('Matt 1:1; John 1:1; John 2:2'), 'Matt 1:1; John 1:1; 2:2')

   def test_consolidateSameChapter(self):
      self.assertEqual(consolidate('John 1:1; John 1:2'), 'John 1:1,2')
      self.assertEqual(consolidate('Gen 1:1; Gen 1:2; Gen 1:3; Gen 2:1; Exod 3:3'), 'Gen 1:1,2,3; 2:1; Exod 3:3')

   def test_consolidateBookWithNumber(self):
      self.assertEqual(consolidate('1 Sam 1:1; 1 Sam 1:3; 1 Sam 2:2; 2 Sam 2:2'), '1 Sam 1:1,3; 2:2; 2 Sam 2:2')

   def test_normalize(self):
      self.assertEqual(normalize('1 John 1:1'), '1John 1:1')
      self.assertEqual(normalize('i John 1:1'), '1John 1:1')
      self.assertEqual(normalize('i. Jn 1:1'), '1Jn 1:1')
      self.assertEqual(normalize('Matt 2:16\u201317,19'), 'Matt 2:16-17,19') # en dash

if __name__ == '__main__':
   suite = unittest.TestLoader().loadTestsFromTestCase(TestVerses)
   unittest.TextTestRunner(verbosity=2).run(suite)
