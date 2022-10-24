from pygame import *
import pygame
import time
import random


init()

gray=(60,60,60)
black=(255,0,0)

fenetre=display.set_mode((640,480))
route = image.load("backstart.jpg").convert()
fenetre.blit(route, (0,0))


voituu = pygame.image.load("voituu.png").convert_alpha()
position_voituu = voituu.get_rect()
fenetre.blit(voituu, (300, 300))
voituu = pygame.transform.scale(voituu, (55, 100))


display.flip()

play=1
while play:
    for event in pygame.event.get():
        if event.type == QUIT:
            play = 0

        if event.type == KEYDOWN:
                if event.key == K_q:
                    position_voituu = position_voituu.move(-10,0)
                if event.key == K_d:
                    position_voituu = position_voituu.move(10,0)

    fenetre.blit(route, (0,0))
    fenetre.blit(voituu, position_voituu)

    pygame.display.flip()
