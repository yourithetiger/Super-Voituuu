from pygame import *
import pygame # certaines fontions ne fonctionennent pas sans le "pygame."
from cons import *

init()
clock = time.Clock()
fenetre=display.set_mode((fenetre_x,fenetre_y))
display.set_caption(titre)

#fond
fond = image.load("fond.jpg").convert()
fenetre.blit(fond, (-400,0))
#route
route = image.load("route.jpg").convert()
fenetre.blit(route, (300,0))
route_y = 0

#voiture
car = image.load("voituuu.png").convert_alpha()
car_pos =  car.get_rect()
fenetre.blit(car, car_pos)
car = pygame.transform.smoothscale(car, (100, 200))

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
    route_y += 1
    if route_y > 763:
        route_y = 0
    fenetre.blit(fond, (-400,0))
    fenetre.blit(route, (300, route_y))
    fenetre.blit(route, (300, route_y - 763))
    fenetre.blit(car, car_pos)
    display.flip()

