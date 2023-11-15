import unittest
from src.SampleClass import SampleClass

class TestSampleClass(unittest.TestCase):
    def setUp(self):
        self.class1 = SampleClass(1,2)
        self.class2 = SampleClass(3,4)
        self.add = self.class1 + self.class2
        self.sub = self.class1 - self.class2

    def test_add(self):
        self.assertEqual(self.add.x, 4)
        self.assertEqual(self.add.y, 6)

    def test_sub(self):
        self.assertEqual((self.class1 - self.class2).x, -2)
        self.assertEqual((self.class1 - self.class2).y, -2)