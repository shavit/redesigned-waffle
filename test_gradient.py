import unittest
from graphics.gradient import Gradient

class TestGradient(unittest.TestCase):

    def testCreateGradient(self):
        g = Gradient()
        self.assertNotEqual(g, None)
        # self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
