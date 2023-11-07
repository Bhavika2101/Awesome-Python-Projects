import unittest
from unittest.mock import Mock
from game import Ball
from tkinter import *


class TestBall(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=500, height=500)
        bricks = [[Mock() for b in range(5)] for l in range(5)]
        paddle = Mock()
        score = Mock()

        self.ball = Ball(self.canvas, 'blue', paddle, bricks, score)
        self.root.mainloop()

    def tearDown(self):
        self.root.destroy()
       
    def test_brick_hit_all_miss(self):
        # Scenario 1: All Brick Miss Scenario
        self.ball.canvas.coords = Mock(return_value=[10, 10, 20, 20])
        pos = [50, 50, 60, 60]
        self.assertFalse(self.ball.brick_hit(pos))
    
    def test_brick_hit_single_brick(self):
        # Scenario 2: Single Brick Hit Scenario
        self.ball.canvas.coords = Mock(return_value=[50, 50, 60, 60])
        pos = [55, 55, 70, 70]
        self.assertTrue(self.ball.brick_hit(pos))
        self.assertEqual(self.ball.score.configure.call_args[0][0], 'Score: 1')
        self.assertEqual(self.ball.hit, 1)

    def test_brick_hit_multiple_bricks(self):
        # Scenario 3: Multiple Bricks Hit Scenario
        self.ball.canvas.coords = Mock(return_value=[55, 55, 70, 70])
        pos = [30, 30, 75, 75]
        self.assertTrue(self.ball.brick_hit(pos))
        self.assertEqual(self.ball.score.configure.call_args[0][0], 'Score: 5')
        self.assertEqual(self.ball.hit, 5)
        
    def test_brick_hit_bell_function(self):
        # Scenario 4: Testing 'bell' Function
        # More information needed about how `ball.brick_hit` calls 'bell' function.
        pass

    def test_brick_hit_empty_brick_line(self):
        # Scenario 5: Brick Line Empty Scenario
        self.ball.bricks = []
        pos = [50, 50, 60, 60]
        self.assertFalse(self.ball.brick_hit(pos))

    def test_brick_hit_exception(self):
        # Scenario 6: Exception Scenario
        self.ball.canvas.coords = Mock(side_effect=Exception("Brick Position Error"))
        pos = [50, 50, 60, 60]
        self.assertFalse(self.ball.brick_hit(pos))


if __name__ == "__main__":
    unittest.main(verbosity=2)
