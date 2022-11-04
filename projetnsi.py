from pygame import *
import pygame # certaines fontions ne fonctionennent pas sans le "pygame."
from cons import *
from classes import *
import random

init()
clock = time.Clock()
fenetre=display.set_mode((fenetre_x,fenetre_y))
display.set_caption(titre)

def main():
  game = Game()
  play=1
  while play:
      for event in pygame.event.get(): 
        if event.type == QUIT:
          play = 0         
      clock.tick(120)
      touche = pygame.key.get_pressed()
      game.play(fenetre, touche) 
      if game.dead:
        menu(death_count=game.Deathcount)     
      display.flip()
      
def menu(death_count):
    global points
    run = True

    while run:
        fenetre.fill((255, 255, 255))


        if death_count == 0:
            text = fonte.render("Press any Key to Start", True, Black)
        elif death_count > 0:
            text = fonte.render("Press any Key to Restart", True, Black)
            score = fonte.render("bravo", True, Black)
            scoreRect = score.get_rect()
            scoreRect.center = (fenetre_x // 2, fenetre_y // 2 + 50)
            fenetre.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (fenetre_x // 2, fenetre_y // 2)
        fenetre.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                main()
        display.flip()
menu(death_count=0)
test=0