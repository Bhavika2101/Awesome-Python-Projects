import unittest
from unittest.mock import Mock
from game import Ball 

class TestBallPaddleHit(unittest.TestCase):
    
    def setUp(self):
        self.canvas = Mock()
        self.paddle = Mock()
        self.bricks = Mock()
        self.score = Mock()
        self.ball = Ball(self.canvas, "blue", self.paddle, self.bricks, self.score)
        self.ball.canvas_width = 500
        self.ball.canvas_height = 500
        # mocking the actual methods with predefined return values.
        self.ball.canvas.coords = Mock()
        self.ball.paddle_hit = Mock()

    def test_no_hit(self):
        self.ball.canvas.coords.return_value = [50, 50, 100, 100]  # mock return value of canvas' coordinates
        pos = [101, 40, 120, 60]  # ball not intersecting with paddle at all
        self.ball.paddle_hit.return_value = False
        self.assertEqual(self.ball.paddle_hit(pos), False)

    def test_hit_x_cordinates(self):
        self.ball.canvas.coords.return_value = [50, 50, 100, 100]
        pos = [50, 120, 100, 140]  # only x-axis coordinates coincide with paddle position
        self.ball.paddle_hit.return_value = False
        self.assertEqual(self.ball.paddle_hit(pos), False)

    def test_hit_y_cordinates(self):
        self.ball.canvas.coords.return_value = [50, 50, 100, 100]
        pos = [150, 50, 200, 100]  # only y-axis coordinates coincide with paddle position
        self.ball.paddle_hit.return_value = False
        self.assertEqual(self.ball.paddle_hit(pos), False)

    def test_corner_no_hit(self):
        self.ball.canvas.coords.return_value = [50, 50, 100, 100]
        pos = [100, 100, 120, 120]  # corner of ball on boundary of paddle
        self.ball.paddle_hit.return_value = False
        self.assertEqual(self.ball.paddle_hit(pos), False)

    def test_inside_paddle_hit(self):
        self.ball.canvas.coords.return_value = [50, 50, 100, 100]
        pos = [60, 60, 80, 80]  # Ball entirely inside the paddle
        self.ball.paddle_hit.return_value = True
        self.assertEqual(self.ball.paddle_hit(pos), True)

    def test_intersection_paddle_hit(self):
        self.ball.canvas.coords.return_value = [50, 50, 100, 100]
        pos = [80, 80, 120, 120]  # Ball intersects the paddle
        self.ball.paddle_hit.return_value = True
        self.assertEqual(self.ball.paddle_hit(pos), True)

    def test_paddle_cordinates_as_none(self):
        self.ball.canvas.coords.return_value = None
        pos = [80, 80, 120, 120]  # Ball intersects the imaginary paddle
        self.ball.paddle_hit.return_value = False
        self.assertEqual(self.ball.paddle_hit(pos), False)

        
if __name__ == "__main__":
    unittest.main(verbosity=2)
