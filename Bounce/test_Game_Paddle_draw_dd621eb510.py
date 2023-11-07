from tkinter import Tk
from game import Game  # Assuming you have a Game class in game.py that takes root as an argument

root = Tk()
game_instance = Game(root)
root.mainloop()
