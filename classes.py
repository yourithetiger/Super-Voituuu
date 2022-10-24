from pygame import *
from pygame.locals import * 
from cons import *

class Joueur:
    def __init__(self, score):
        self.x = 0
        self.y = 0
        self.score = 0
    def deplacer(self, dir):
        