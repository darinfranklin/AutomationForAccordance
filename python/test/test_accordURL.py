#!/usr/bin/python
import unittest
from verses import accordURL

class TestAccordURL(unittest.TestCase):
   def test_accordURL(self):
      self.assertEqual(accordURL(u'KJVS', u'Matt 1:1'), 
            'accord://read/KJVS?Matt_1:1')

   def test_accordURLEscape(self):
      self.assertEqual(accordURL(u'Torah\u00b0', u'Matt\u00b0 1:1; John 1:1,2,3; Acts 1.1'), 
            'accord://read/Torah%C2%B0?Matt%C2%B0_1:1;_John_1:1,2,3;_Acts_1.1')

if __name__ == '__main__':
   suite = unittest.TestLoader().loadTestsFromTestCase(TestAccordURL)
   unittest.TextTestRunner(verbosity=2).run(suite)
