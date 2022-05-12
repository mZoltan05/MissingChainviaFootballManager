from django.test import TestCase
#from Logic import Logic 
import unittest
from home.models import Player, Score

# Create your tests here.
def add(a,b):
    return a+b

class TestAdd(unittest.TestCase):
     def test_add(self):
          self.assertEqual(add(2, 4), 6)

if __name__ == '__main__':
    unittest.main()
