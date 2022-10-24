from pygame import *
import time
import random


init()

gray=(60,60,60)
black=(255,0,0)

fenetre=display.set_mode((640,480))
display.set_caption("voituu")
route = image.load("backstart.jpg").convert()
fenetre.blit(route, (0,0))

voituu = pygame.image.load("voituu").convert_alpha()
fenetre.blit(voituu, (250,300))


play=1
while play:
    display.flip()
    for event in event.get():
        if event.type == QUIT:
            play = 0