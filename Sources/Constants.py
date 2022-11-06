import pygame

from pygame import *

pygame.init()
resolution = (1600,920)
window = pygame.display.set_mode(resolution)

gameWidth = window.get_width()
gameHeight = window.get_height()
gameTitle = "Voituuu"
gameSpeed = 5

drawHitBox = False

blackColor = (0,0,0)
whiteColor = (255,255,255)
redColor = (255,0,0)
greenColor = (0,255,0)
blueColor = (0,0,255)

mainFont = font.Font('freesansbold.ttf', 30)

perso1 = image.load("../nsipoo/Assets/player/perso1.png")
perso1 = transform.smoothscale(perso1, (60, 140))

perso2 = image.load("../nsipoo/Assets/player/perso2.png")
perso2 = transform.smoothscale(perso2, (70, 140))

perso3 = image.load("../nsipoo/Assets/player/perso3.png")
perso3 = transform.smoothscale(perso3, (65, 140))

perso4 = image.load("../nsipoo/Assets/player/perso4.png")
perso4 = transform.smoothscale(perso4, (70, 140))

perso5 = image.load("../nsipoo/Assets/player/perso5.png")
perso5 = transform.smoothscale(perso5, (70, 140))