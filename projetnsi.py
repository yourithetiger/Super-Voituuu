from pygame import *
import pygame #
import time
import random

init()
clock = pygame.time.Clock()
fenetre_x = 1440
fenetre_y = 864
fenetre=display.set_mode((fenetre_x,fenetre_y))
display.set_caption("voituuu")

#fond
fond = image.load("backstart.jpg").convert()
fenetre.blit(fond, (0,0))
fond_y = 0

#voiture
car = image.load("voituuu.png").convert_alpha()
car_pos =  car.get_rect()
fenetre.blit(car, car_pos)
display.flip()
key.set_repeat(50, 2)
play=1
while play:

    for event in pygame.event.get():
        if event.type == QUIT:
            play = 0
        if event.type == KEYDOWN:
            if event.key == K_q:
                    car_pos = car_pos.move(-1,0)
            if event.key == K_d:
                    car_pos = car_pos.move(1,0)

    clock.tick(60)
    fond_y += 1
    if fond_y > 864:
        fond_y = 0
    fenetre.blit(fond, (0, fond_y))
    fenetre.blit(fond, (0, fond_y - 864))
    fenetre.blit(car, car_pos)
    display.flip()

