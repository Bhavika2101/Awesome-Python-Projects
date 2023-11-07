import unittest
from unittest.mock import MagicMock, patch

# Ensure 'game' module has the class 'Paddle'
from game import Paddle

class TestPaddleTurnRight(unittest.TestCase):
    def setUp(self):
        self.canvas = MagicMock()
        self.color = "red"
        self.paddle = Paddle(self.canvas, self.color)
        self.paddle.x = 0  

    def test_paddle_turn_right_without_any_event(self):
        self.paddle.turn_right(None)
        self.assertEqual(self.paddle.x, 0, "Paddle's x value should retain its default value")
     
    def test_paddle_turn_right_on_right_turn_event(self):
        event = MagicMock() 
        self.paddle.turn_right(event)
        self.assertEqual(self.paddle.x, 3.5, "The paddle's x value did not change as expected on right turn event")

    # More Test Cases

if __name__ == "__main__":
    unittest.main(verbosity=3)
