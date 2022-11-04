import random
from pygame import *
import pygame
from pygame.locals import * 
from cons import *


class Game:
    
    def __init__(self):
        self.Deathcount = 0
        self.player = Player()
        self.background = image.load("fond.jpg").convert()
        self.background = transform.smoothscale(self.background, (fenetre_x, 1080*multiplier))
        self.road = Road()
        self.ObsLeft = []
        self.ObsRight = []
        self.Obstacles = []
        self.dead = 0
        self.score = Score()
        self.LeftTime = 0
        self.RightTime = 0
        
    def play(self, fenetre, touche):
        fenetre.blit(self.background, (0,0))
        self.road.defil(fenetre)
        self.player.draw(fenetre)
        self.deplacement(touche)
        self.obsspawn(fenetre)
        self.score.draw(fenetre)
        self.LeftTime -= 1
        self.RightTime -= 1 
            
    def deplacement(self, touche):
        if touche[K_q] and not self.player.rect.x < self.road.x_left:
                self.player.move(-1)
        if touche[K_d] and not self.player.rect.x > self.road.x_right - self.player.rect.width:
            self.player.move(1)
    
    def obsspawn(self,fenetre):
        if len(self.ObsLeft) < 3 and self.LeftTime == 0 :
            self.ObsVoie = random.randint(0,1)
            if self.ObsVoie :
                self.ObsPos = (self.road.x_right-190*multiplier,-250*multiplier) 
            else :
                self.ObsPos = (self.road.x_right-100*multiplier,-250*multiplier) 
            self.ObsLeft.append(Obstacle(self.ObsPos,1))
            self.LeftTime = random.randint(80,150)
        if self.RightTime == 0 :
            self.ObsVoie = random.randint(0,1)
            if self.ObsVoie :
                  self.ObsPos = (self.road.x_left+30*multiplier,-250*multiplier)
            else :
                  self.ObsPos = (self.road.x_left+120*multiplier,-250*multiplier) 
            self.ObsRight.append(Obstacle(self.ObsPos,0))
            self.RightTime = random.randint(80,150)
        self.obsupdate(fenetre, self.ObsLeft)
        self.obsupdate(fenetre, self.ObsRight)
        
    def obsupdate(self,fenetre, LoR):
            for obs in LoR:
             obs.draw(fenetre)
             obs.update()
             if obs.rect.y > fenetre_y-obs.rect.height:
                LoR.remove(obs)
                if self.player.rect.x < fenetre_x/2:
                    self.score.update(2)
                else:
                    self.score.update(1)
             self.col(obs)
             
    def col(self, obs):
        if self.player.rect.colliderect(obs.rect):
            self.dead = 1
            self.Deathcount += 1
            
  
 
class Road:
    
    def __init__(self):
        self.image = image.load("route.jpg").convert()
        self.image = transform.smoothscale(self.image, (400*multiplier, fenetre_y))
        self.rect = self.image.get_rect()
        self.x_left = (fenetre_x/2) - (self.rect.width/2)
        self.x_right = (fenetre_x/2) + (self.rect.width/2)
        self.rect.x = self.x_left
        self.rect.y = fenetre_y
        self.rect2 = self.rect
        self.rect2.y -= fenetre_y
    def defil(self, screen):
        self.rect = self.rect.move(0,GameSpeed)
        if self.rect.y > fenetre_y:
            self.rect.y = 0
        self.rect2.y = self.rect.y - fenetre_y
        screen.blit(self.image, self.rect)
        screen.blit(self.image,self.rect2)

        
        
         
class Player(sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.score = 0
        self.image = image.load("voituuu.png").convert_alpha()
        self.image = transform.smoothscale(self.image, (70*multiplier, 140*multiplier))
        self.rect = self.image.get_rect()
        self.rect.x = fenetre_x/2
        self.rect.y = 500*multiplier
        self.speed = 10

    def move(self, dir):
        self.rect = self.rect.move(dir*self.speed,0)
    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Obstacle(sprite.Sprite):
    def __init__(self, pos, sens):
        super().__init__()
        self.image = image.load("voituuu.png").convert_alpha()
        self.image = transform.smoothscale(self.image, (70*multiplier, 140*multiplier))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos)
        self.sens = sens
        self.speed = 0
        if self.sens :
            self.speed += GameSpeed - 1
        else :
            self.image = transform.rotate(self.image, 180)
            self.speed = GameSpeed + 1
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)
    
    def update(self):
            self.rect.y += self.speed

class Score():
    def __init__(self):
        self.point = 0
        self.font = font.Font('freesansbold.ttf', 20)
        self.text = fonte.render("Score: " + str(self.point), True, Red)
        self.textRect = self.text.get_rect()
        self.textRect.center = (100,100)
    def update(self, bonus):
        self.point += bonus
        self.text = fonte.render("Score: " + str(self.point), True, Red)
    def draw(self, SCREEN):
        SCREEN.blit(self.text, self.textRect)
        