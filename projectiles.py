from graphics import *
from random import *
from string import *
class Projectiles:
    def __init__(self, lives, time):
        timeLimit = 0
        self.lives = lives
        self.timer = time

    def Spawning(self,win,timer):
        textBox = Text(Point(320,200), "Type or Perish: ")
        textBox.draw(win)
        score = 0
        timeLimit = 0
        while(self.lives != 0):
            spawn = randrange(380)
            projectiles = Text(Point(400,200),choice(ascii_lowercase))
            livesTxt = Text(Point(560,25),"Lives: " + str(self.lives))
            livesTxt.draw(win)
            projectiles.draw(win)
            projectiles.setSize(20)
            while(timeLimit <= timer):
                time.sleep(0.5)
                timeLimit = timeLimit + 1
                x = win.checkKey()
                if(x == projectiles.getText()):
                    projectiles.setTextColor("green")
                    score += 1
                    time.sleep(2)
                    projectiles.setText(choice(ascii_lowercase))
                    projectiles.setTextColor("black")
                    timeLimit = 0

                    livesTxt.setText("Lives: " + str(self.lives))
                    projectiles.setTextColor("black")

                if(timeLimit >= timer):
                    self.lives = self.lives - 1
                    projectiles.setTextColor("red")
                    time.sleep(2)
                    projectiles.setTextColor("black")
                    projectiles.setText(choice(ascii_lowercase))
                    timeLimit = 0
                    livesTxt.setText("Lives: " + str(self.lives))
                    update(10)
                
                if(self.lives == 0):
                    projectiles.setText(choice("PERISHED"))
                    textBox.setText("Score: " + str(score) + "\n Click To Exit")
                    win.getMouse()
                    win.close()
                    
                
            