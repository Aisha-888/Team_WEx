// libraries
import cmd
import textwrap
import sys
import os
import time
import random
screen_width = 100

// Player Class
class player:
    def __init__(self):
        self.name = ''
        self.feeling = ''
        self.astrological = ''
        self.position = 'ground'
        self.won = False
        self.solves = 0
player1 = player()
