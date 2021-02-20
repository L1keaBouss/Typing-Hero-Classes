import os
from game import *
from projectiles import *


try:
    from graphics import *
except:
    # implement pip as a subprocess:
    print("Downloaded Graphics.py")
    os.system("pip3 install graphics.py")
finally:
    from graphics import *
    print("Done!\n")

def main():
    try:
        lives = int(input("Enter lives amount: "))
    except ValueError:
        try:
            lives =  int(input("ERROR: Enter a Number for Lives: "))
        except ValueError:
            print("Error, Exiting Program")

    try:
        time = int(input("Enter time amount: "))
    except ValueError:
        try:
            time =  int(input("ERROR: Enter a Number seconds: "))
        except ValueError:
            print("Error, Exiting Program")
    gamer = Game(lives,time)
    gamer.gameplay()
    pass
main()