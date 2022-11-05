from pygame import *
import pygame # certaines fontions ne fonctionennent pas sans le "pygame."
from Constants import *
from Builder import *
from SoundManager import *

pygame.init()
clock = time.Clock()
display.set_caption(gameTitle)
deathImage = pygame.image.load("../nsipoo/Assets/images/deathmenu.png")
deathImage = transform.scale(deathImage, (gameWidth, gameHeight))

boutonPlay = pygame.Rect(gameWidth/2 - 140/2 - 100, gameHeight/2 - 40/2 + 35, 140, 40)
boutonQuit = pygame.Rect(gameWidth/2 - 140/2 + 100, gameHeight/2 - 40/2 + 35, 140, 40)

gameOverSound = SoundManger(0.2, "../nsipoo/Assets/sounds/gameOver.wav")

def main():
  game = Game()

  while game.STATE != GameState.QUIT:
    mousePos = mouse.get_pos()

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: game.STATE = GameState.QUIT

      if event.type == MOUSEBUTTONDOWN:
        if(checkBoutonHover(boutonPlay, mousePos)):
          game.STATE = GameState.PLAY

        if(checkBoutonHover(boutonQuit, mousePos)):
          game.STATE = GameState.QUIT


    if game.STATE == GameState.QUIT: pygame.quit()
    if game.STATE == GameState.MENU: menu(game, mousePos)
    if game.STATE == GameState.DEAD: 
      menu(game, mousePos)

    if game.STATE == GameState.PLAY:
        clock.tick(120)

        keyListener = pygame.key.get_pressed()
        if(keyListener[K_k]): drawHitBox = True

        game.play(window, keyListener) 
        display.flip()

        if game.isOver: game.STATE = GameState.DEAD

def menu(game, mousePos):
    window.fill(blackColor)

    if game.Deathcount == 0:
        text = mainFont.render("Press any Key to Start", True, whiteColor)
        window.blit(text, (gameWidth / 2 - text.get_width() / 2, gameHeight / 2 - text.get_height()))

        if(checkBoutonHover(boutonPlay, mousePos)):  draw.rect(window, whiteColor, boutonPlay)
        else: draw.rect(window, redColor, boutonPlay)

        if(checkBoutonHover(boutonQuit, mousePos)):  draw.rect(window, whiteColor, boutonQuit)
        else: draw.rect(window, redColor, boutonQuit)

        playText = mainFont.render('Play', True, blackColor)
        window.blit(playText, (boutonPlay.x + boutonPlay.width /2 - playText.get_width()/2, boutonPlay.y + boutonPlay.height /2 - playText.get_height()/2))

        quitText = mainFont.render('Quit', True, blackColor)
        window.blit(quitText, (boutonQuit.x + boutonQuit.width /2 - quitText.get_width()/2, boutonQuit.y + boutonQuit.height /2 - quitText.get_height()/2))

    elif game.Deathcount > 0:
        gameOverSound.play()

        window.blit(deathImage, (0,0))
        text = mainFont.render("Press any Key to Restart", True, whiteColor)
        window.blit(text, (gameWidth / 2 - text.get_width() / 2, gameHeight / 2 - text.get_height()))

        score = mainFont.render("Current Score = " + str(game.score.point), True, whiteColor)
        scoreRect = score.get_rect()
        scoreRect.center = (gameWidth / 2, gameHeight / 2 + 50)
        window.blit(score, scoreRect)

    textRect = text.get_rect()
    textRect.center = (gameWidth // 2, gameHeight // 2)

    display.flip()

def checkBoutonHover(button, mousePos):
  if button.collidepoint(mousePos[0], mousePos[1]):
    return True
  else: 
    return False

main()