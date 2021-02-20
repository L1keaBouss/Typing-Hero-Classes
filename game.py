import time
import string
from graphics import *
from projectiles import *


class Game:
    def __init__(self, lives, time):
        self.lives = lives
        self.time = time

    def gameplay(self):
        win = GraphWin("Typing Hero",600,400)
        folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(folder, 'human.gif')
        protect = Image(Point(50, 200),my_file)
        protect.draw(win)
        livesTxt = Text(Point(560,25),"Lives: " + str(self.lives))
        livesTxt.draw(win)
        letters = Projectiles(self.lives, self.time)
        letters.Spawning(win,self.time)
            
