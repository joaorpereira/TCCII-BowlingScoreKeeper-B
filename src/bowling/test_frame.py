import unittest
from .frame import Frame

class TestFrames(unittest.TestCase):
    def test_score(self):
        self.assertEqual(Frame.score(2, 3), 5)

    def test_score(self):
        self.assertEqual(Frame.is_strike(10, 0), 10)

    def test_score(self):
        self.assertEqual(Frame.is_spare(5, 5), 10)

if __name__ == '__main__':
    unittest.main()
