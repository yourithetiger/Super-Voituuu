from pygame import *
import time
import random


init()

gray=(60,60,60)
black=(255,0,0)

fenetre=display.set_mode((640,480))
display.set_caption("voituuu")
sol = image.load("backstart.jpg").convert()
fenetre.blit(sol, (0,0))

play=1
while play:
    display.flip()
    for event in event.get():
        if event.type == QUIT:
            play = 0
            
    


