import unittest
from game.knight import Knight
from game.road import Road

class TestKnight(unittest.TestCase):
    
    def test_create_knight(self):
        knight = Knight(Road(10, None), 0, None)
        knight.tick()


if __name__ == '__main__':
    unittest.main()