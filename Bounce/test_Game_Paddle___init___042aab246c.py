import unittest
from unittest.mock import MagicMock, call
from tkinter import Tk, Canvas
from game import Paddle  # Ensure this import is correctly setup

class TestPaddleInit(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_rectangle = MagicMock()
        self.canvas.move = MagicMock()
        self.canvas.bind_all = MagicMock()
        self.canvas.winfo_width = MagicMock()
        self.canvas.winfo_width.return_value = 500

    def tearDown(self):
        self.root.quit()

    def test_init(self):
        paddle = Paddle(self.canvas, 'blue')
        self.canvas.create_rectangle.assert_called_with(0, 0, 100, 10, fill='blue')
        self.canvas.move.assert_called_with(paddle.id, 200, 485)
        self.assertEqual(paddle.x, 0)
        self.assertEqual(paddle.pausec, 0)
        self.canvas.winfo_width.assert_called_once()
        self.assertEqual(paddle.canvas_width, 500)
        self.canvas.bind_all.assert_has_calls([call("<Left>", paddle.turn_left), 
                                               call("<Right>", paddle.turn_right), 
                                               call("<space>", paddle.pauser)])

    def test_paddle_color(self):
        # check various colors
        colors = ['red', 'blue', 'green', 'black', 'white']
        for color in colors:
            with self.subTest(color=color):
                paddle = Paddle(self.canvas, color)
                self.canvas.create_rectangle.assert_called_with(0, 0, 100, 10, fill=color)

    def test_canvas_width(self):
        # check various canvas widths
        widths = [100, 200, 300, 400, 500]
        for width in widths:
            with self.subTest(width=width):
                self.canvas.winfo_width.return_value = width
                paddle = Paddle(self.canvas, 'blue')
                self.assertEqual(paddle.canvas_width, width)

    def test_no_exceptions(self):
        try:
            paddle = Paddle(self.canvas, 'blue')
            paddle.turn_left('<Left>')
            paddle.turn_right('<Right>')
            paddle.pauser('<space>')
        except Exception as e:
            self.fail(f"Test raised exception {e}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
