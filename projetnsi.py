from pygame import *
import pygame # certaines fontions ne fonctionennent pas sans le "pygame."
from cons import *
from classes import *

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
    
    
    
  background pygame.image.load('ressource/fond.jpg')

background.convert()


y_background = 1

running = True



running True

while running:

y_background +- 1



if y_background < 619:

screen.blit(background, (-109, y_background))

screen.blit(background, (-109, y_background-619))

else:

y_background-e

screen.blit(background, (-109, y_background))

screen.blit(player.image, player.rect)

clock.tick(60)
print(f"{clock.get_fps()FPS }")

pygame.display.flip()


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_widht

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
       screen.blit(self.image[self.type], self.rect)
          
          

            
    


