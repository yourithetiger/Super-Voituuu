from pygame import *
import pygame # certaines fontions ne fonctionennent pas sans le "pygame."
from cons import *
from classes import Game, Road, Player

init()

     

clock = time.Clock()
fenetre=display.set_mode((fenetre_x,fenetre_y))
display.set_caption(titre)


display.flip()

game = Game()
play=1
while play:
    clock.tick(120)
    fenetre.blit(game.background, (-400,0))
    fenetre.blit(game.road.image, game.road.rect)
    fenetre.blit(game.road.image, game.road.rect2)
    fenetre.blit(game.player.image, game.player.rect)
    game.road.defil()
    
    
    if game.pressed.get(K_q):
                 game.player.move(-1)
    if game.pressed.get(K_d):
                 game.player.move(1)
                 
                 
    for event in pygame.event.get():
        
        if event.type == QUIT:
            play = 0
        if event.type == KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == KEYUP:
            game.pressed[event.key] = False
            
    display.flip()