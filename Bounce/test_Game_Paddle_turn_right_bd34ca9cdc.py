class TestPaddleTurnRight(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.paddle = Paddle(self.canvas, "Blue")

    def test_paddle_turns_right(self):
        # Assuming the game has started and not ended
        self.paddle.game_started = True
        self.paddle.game_ended = False
        self.paddle.turn_right(None)
        self.assertEqual(self.paddle.x, 3.5)

    def test_multiple_right_turns_dont_change_speed(self):
        # Assuming the game has started and not ended
        self.paddle.game_started = True
        self.paddle.game_ended = False
        self.paddle.turn_right(None)
        initial_speed = self.paddle.x
        self.paddle.turn_right(None)
        self.assertEqual(self.paddle.x, initial_speed)
        self.assertEqual(self.paddle.x, 3.5)

    def test_border_limitation(self):
        # Assuming the game has started and not ended
        self.paddle.game_started = True
        self.paddle.game_ended = False
        # TODO: set the paddle position x to the end boundary
        self.paddle.turn_right(None)
        self.assertEqual(self.paddle.x, 3.5)

    def test_pause_resume(self):
        self.paddle.pausec = 1
        # Assuming the game has started and not ended
        self.paddle.game_started = True
        self.paddle.game_ended = False
        # TODO: add function to pause and then unpause the game
        self.paddle.turn_right(None)
        self.assertEqual(self.paddle.x, 3.5)

    def test_move_before_game_start(self):
        # Simulating game not started yet
        self.paddle.game_started = False
        self.paddle.game_ended = False
        self.paddle.x = 0
        self.paddle.turn_right(None)
        self.assertEqual(self.paddle.x, 0)

    def test_move_after_game_end(self):
        # Simulating game has ended
        self.paddle.game_started = False 
        self.paddle.game_ended = True
        self.paddle.x = 0
        self.paddle.turn_right(None)
        self.assertEqual(self.paddle.x, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
