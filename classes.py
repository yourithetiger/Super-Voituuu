import random
from pygame import *
from pygame.locals import * 
from cons import *

class Game:
    
    def __init__(self):
        self.player = Player()
        self.background = image.load("fond.jpg").convert()
        self.road = Road()
        self.pressed = {}

class Road:
    
    def __init__(self):
        self.image = image.load("route.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 763
        self.rect2 = self.rect
        self.rect2.y -= 763
    def defil(self):
        self.rect = self.rect.move(0,1)
        if self.rect.y > 763:
            self.rect.y = 0
        self.rect2.y = self.rect.y - 763
        
         
class Player(sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.score = 0
        self.image = image.load("voituuu.png").convert_alpha()
        self.image = transform.smoothscale(self.image, (100, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.speed = 5

    def move(self, dir):
        if dir == 1 and not self.rect.x > 856:
            self.rect = self.rect.move(dir*self.speed,0)
        elif dir == -1 and not self.rect.x < 300:
            self.rect = self.rect.move(dir*self.speed,0)


class Obstacle(sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = image.load("voituuu.png").convert_alpha()
        self.image = transform.smoothscale(self.image, (100, 200))

        self.rect = self.image.get_rect()
        self.rect.x = random