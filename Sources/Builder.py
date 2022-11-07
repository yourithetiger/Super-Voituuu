import random
from pygame import *
import pygame
from pygame.locals import * 
from Constants import *
from enum import Enum

class GameState(Enum):
    PLAY = 1
    QUIT = 2
    DEAD = 3
    MENU = 4
    RUN = 0

class Game:
    def __init__(self):
        self.STATE = GameState.MENU
        self.Deathcount = 0
        self.player = Player()
        self.background = image.load("../nsipoo/Assets/images/fond.jpg").convert()
        self.background = transform.smoothscale(self.background, (gameWidth, gameHeight))
        self.road = Road()
        self.ObsLeft = []
        self.ObsRight = []
        self.Obstacles = []
        self.isOver = 0
        self.score = Score()
        self.LeftTime = 0
        self.RightTime = 0
        
    def play(self, window, keyBind):
        window.blit(self.background, (0,0))
        self.road.defil(window)
        self.player.draw(window)
        self.deplacement(keyBind)
        self.obsspawn(window)
        self.score.draw(window)
        self.LeftTime -= 1
        self.RightTime -= 1 
        
            
    def deplacement(self, keyBind):
        if keyBind[K_q] and not self.player.hitbox.x < self.road.x_left: self.player.move(-0.6)
        if keyBind[K_d] and not self.player.hitbox.x > self.road.x_right - self.player.hitbox.width: self.player.move(0.6)
    
    def obsspawn(self, window):
        if self.LeftTime == 0 :
            self.ObsVoie = random.randint(0,1)

            if self.ObsVoie : self.ObsPos = (self.road.x_right-185,-250) 
            else : self.ObsPos = (self.road.x_right-82,-250) 

            self.ObsLeft.append(Obstacle(self.ObsPos,1))
            self.LeftTime = random.randint(120,180)

        if self.RightTime == 0 :
            self.ObsVoie = random.randint(0,1)

            if self.ObsVoie : self.ObsPos = (self.road.x_left+15,-250)
            else : self.ObsPos = (self.road.x_left+115,-250) 

            self.ObsRight.append(Obstacle(self.ObsPos,0))
            self.RightTime = random.randint(90,150)

        self.obsupdate(window, self.ObsLeft)
        self.obsupdate(window, self.ObsRight)
        
    def obsupdate(self,window, LoR):
            for obs in LoR:
             obs.draw(window)
             obs.update()

             if obs.hitbox.y > gameHeight + obs.hitbox.height:
                LoR.remove(obs)
                if self.player.hitbox.x < gameWidth/2: self.score.update(2)
                else: self.score.update(1)

             self.col(obs)
             
    def col(self, obs):
        if self.player.hitbox.colliderect(obs.hitbox):
            gameOverSound.play().set_volume(0.2)
            self.STATE = GameState.DEAD
            self.Deathcount += 1
            
class Road:
    def __init__(self):
        self.image = image.load("../nsipoo/Assets/images/route.jpg").convert()
        self.image = transform.smoothscale(self.image, (400, gameHeight))
        self.rect = self.image.get_rect()
        self.x_left = (gameWidth/2) - (self.rect.width/2)
        self.x_right = (gameWidth/2) + (self.rect.width/2)
        self.rect.x = self.x_left
        self.rect.y = gameHeight
        self.rect2 = self.rect
        self.rect2.y -= gameHeight

    def defil(self, screen):
        self.rect = self.rect.move(0, gameSpeed)
        if self.rect.y > gameHeight: self.rect.y = 0
        self.rect2.y = self.rect.y - gameHeight
        screen.blit(self.image, self.rect)
        screen.blit(self.image,self.rect2)

class Player(sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.score = 0
        self.speed = 10
        self.speed = 10

    def initType(self, type):
        self.type = type
        if self.type == 1: self.image = image.load("../nsipoo/Assets/player/perso1.png")
        elif self.type == 2: self.image = image.load("../nsipoo/Assets/player/perso2.png")
        elif self.type == 3: self.image = image.load("../nsipoo/Assets/player/perso3.png")
        elif self.type == 4: self.image = image.load("../nsipoo/Assets/player/perso4.png")
        elif self.type == 5: self.image = image.load("../nsipoo/Assets/player/perso5.png")

        self.image = transform.smoothscale(self.image, (70, 140))
        self.hitbox = pygame.Rect(gameWidth/2 - 70 / 2, gameHeight - 140 - 20, 70, 140)
  
    def move(self, dir):
        self.hitbox = self.hitbox.move(dir*self.speed,0)

    def draw(self, screen):
        if drawHitBox: pygame.draw.rect(screen, greenColor, self.hitbox)
        screen.blit(self.image, self.hitbox)


class Obstacle(sprite.Sprite):
    def __init__(self, pos, sens):
        super().__init__()
        self.type = random.randint(1,7)
        
        if self.type == 1: self.image = image.load("../nsipoo/Assets/enemy/car1.png")
        elif self.type == 2: self.image = image.load("../nsipoo/Assets/enemy/car2.png")
        elif self.type == 3: self.image = image.load("../nsipoo/Assets/enemy/car3.png")
        elif self.type == 4: self.image = image.load("../nsipoo/Assets/enemy/car4.png")
        elif self.type == 5: self.image = image.load("../nsipoo/Assets/enemy/car5.png")
        elif self.type == 6: self.image = image.load("../nsipoo/Assets/enemy/car6.png")
        elif self.type == 7: self.image = image.load("../nsipoo/Assets/enemy/car7.png")

        self.image = transform.smoothscale(self.image, (70, 140))
        self.hitbox = pygame.Rect(0, 0, 70, 140)
        self.hitbox = self.hitbox.move(pos)
        self.sens = sens
        
        self.speed = 0
        if self.sens : self.speed += gameSpeed - 1
        else :
            self.image = transform.rotate(self.image, 180)
            self.speed = gameSpeed + 1
        
    def draw(self, screen):
        if drawHitBox == True: pygame.draw.rect(screen, blueColor, self.hitbox)
        screen.blit(self.image, self.hitbox)
    
    def update(self):
            self.hitbox = self.hitbox.move(0, self.speed)

class Score():
    def __init__(self):
        self.point = 0
        self.font = font.Font('freesansbold.ttf', 20)
        self.text = mainFont.render("Score: " + str(self.point), True, redColor)
        self.textRect = self.text.get_rect()
        self.textRect.center = (100,100)

    def update(self, bonus):
        self.point += bonus
        self.text = mainFont.render("Score: " + str(self.point), True, redColor)

    def draw(self, screen):
        screen.blit(self.text, self.textRect)