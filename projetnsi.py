from pygame import *
import pygame # certaines fontions ne fonctionennent pas sans le "pygame."
from cons import *
from classes import *
import random

init()

     

clock = time.Clock()
fenetre=display.set_mode((fenetre_x,fenetre_y))
display.set_caption(titre)


display.flip()

game = Game()

play=1
while play:
    for event in pygame.event.get(): 
      if event.type == QUIT:
        play = 0         
    obstacledelay = random.randint(40,100)
    obstacle = Obstacle(random.randint(0,500))
    clock.tick(120)
    touche = pygame.key.get_pressed()
    game.play(fenetre, touche)      
    display.flip()