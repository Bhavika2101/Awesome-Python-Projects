import unittest
from tkinter import Tk, Canvas
# Assuming Paddle and Bricks classes exists in the respective modules. If not, please import them appropriately
# from paddle import Paddle
# from bricks import Bricks 
from game import Game  # Adjust to your project settings
from random import shuffle

root = Tk()
canvas = Canvas(root)
# Always remember to pack the Canvas
canvas.pack()

class TestGame(unittest.TestCase):
    def setUp(self):
        self.paddle = Paddle(canvas, 'blue')  # instance variable
        self.bricks = Bricks(canvas, 'red')  # instance variable
        self.score = 0  # instance variable
        self.color = "red"  # instance variable
        
        self.game = Game(canvas, self.color, self.paddle, self.bricks, self.score)
        self.start_velocity = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]

    def test___init___b7507c076d(self):
        # Accessing through self
        self.assertEqual(self.game.bricks, self.bricks)
        self.assertEqual(self.game.canvas, canvas)
        self.assertEqual(self.game.paddle, self.paddle)
        self.assertEqual(self.game.score, self.score)

        self.assertEqual(self.game.bottom_hit, False)

        self.assertEqual(self.game.hit, 0)

        self.assertIsNotNone(self.game.id)

        x_pos, y_pos = self._get_position(self.game.id)
        self.assertEqual(x_pos, 230)
        self.assertEqual(y_pos, 461)

        self.assertIn(self.game.x, self.start_velocity)
        self.assertEqual(self.game.y, -self.game.x)

        self.assertEqual(self.game.canvas_height, canvas.winfo_height())
        self.assertEqual(self.game.canvas_width, canvas.winfo_width())
    
    def _get_position(self, id):
        # Accessing canvas through self
        pos_list = self.canvas.coords(id)
        x_pos, y_pos = pos_list[0], pos_list[1]
        return x_pos, y_pos

if __name__ == '__main__':
    unittest.main()
