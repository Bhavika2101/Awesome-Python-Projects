import unittest
from game import Ball
from tkinter import Canvas, Label
from unittest.mock import Mock

class test_Brick_Hit(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas() 
        self.paddle = "paddle_object" # Pseudo value, replace with actual instance
        self.score = Label(text="Score: 0")
        self.color = "red"
        self.bricks = [[Mock(id=1), Mock(id=2)], [Mock(id=3), Mock(id=4)]]
        
    #Test case 1: Brick is hit
    def test_brick_hit_success(self):
        for brick_line in self.bricks:
            for brick in brick_line:
                self.canvas.create_rectangle(10, 10, 20, 20, tags=str(brick.id)) # Creating brick in canvas with `id` as its tag

        ball = Ball(self.canvas, self.color, self.paddle, self.bricks, self.score)
        pos = [15, 15, 25, 25] # Position that intersects brick

        result = ball.brick_hit(pos)
        self.assertEqual(result, True, "Expected result is True when brick is hit")
        self.assertEqual(ball.hit, 1, "Expected 'hit' count to be 1 after hitting a brick")

    #Test case 2: No brick to hit
    def test_brick_hit_fail(self):
        ball = Ball(self.canvas, self.color, self.paddle, self.bricks, self.score)
        pos = [100, 100, 110, 110] # Position where there are no bricks

        result = ball.brick_hit(pos)
        self.assertEqual(result, False, "Expected result is False when no brick is hit")

if __name__ == "__main__":
    unittest.main()