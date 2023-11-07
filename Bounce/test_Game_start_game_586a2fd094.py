import unittest
from unittest.mock import MagicMock, patch, ANY
from tkinter import *
import random
import time
import threading

class TestGame(unittest.TestCase):
    def setUp(self):

        # Run Tkinter in separate thread
        self.root = Tk()
        thread = threading.Thread(target=self.root.mainloop)
        thread.start()
        
        self.canvas = Canvas(self.root, width=500, height=500, bd=0, highlightthickness=0,highlightbackground='Red', bg='Black')
        self.canvas.pack(padx=10, pady=10)
        self.score = Label(height=50, width=80, text='Score: 00', font='Consolas 14 bold')
        self.score.pack(side='left')

        # To see updates made to tkinter components
        self.root.update()
        
        self.playing = False
        self.root.bind_all('<Return>', self.start_game)
        self.paddle = self.create_mock_paddle()
        self.bricks = self.create_mock_bricks()
        # Ball object created using Paddle and Bricks
        self.ball = self.create_mock_ball()

    def create_mock_paddle(self):
        mock_paddle = MagicMock()
        mock_paddle.pausec = 0
        return mock_paddle

    def create_mock_bricks(self):
        bricks = []
        for i in range(0, 5):
            b = []
            for j in range(0, 19):
                tmp = MagicMock()
                tmp.color = "PeachPuff3"
                b.append(tmp)
            bricks.append(b)
        return bricks

    def create_mock_ball(self):
        mock_ball = MagicMock()
        mock_ball.hit = 0
        mock_ball.bottom_hit = False
        mock_ball.color = "red"
        return mock_ball

    def start_game(self, event):
        #function code here 
        
    # Test cases code ...

