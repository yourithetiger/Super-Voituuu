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
menuImage = pygame.image.load("../nsipoo/Assets/images/menu2.png")
menuImage = transform.scale(menuImage, (gameWidth, gameHeight))

boutonCar1 = perso1.get_rect()
boutonCar1 = boutonCar1.move(450, 380)


boutonCar2 = perso2.get_rect()
boutonCar2 = boutonCar2.move(595, 380)


boutonCar3 = perso3.get_rect()
boutonCar3 = boutonCar3.move(768, 380)


boutonCar4 = perso4.get_rect()
boutonCar4 = boutonCar4.move(941, 380)


boutonCar5 = perso5.get_rect()
boutonCar5 = boutonCar5.move(1115, 380)


boutonQuit = pygame.Rect(gameWidth/2 - 140/2, gameHeight/2 - 40/2 + 240, 140, 40)
boutonMENU = pygame.Rect(gameWidth/2 - 250/2, gameHeight/2 - 40/2 + 120, 250, 40)
boutonQuitDeath = pygame.Rect(gameWidth/2 - 140/2, gameHeight/2 - 40/2 + 250, 140, 40)



def main():
  game = Game()

  while game.STATE != GameState.QUIT:
    mousePos = mouse.get_pos()
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: game.STATE = GameState.QUIT

      if event.type == MOUSEBUTTONDOWN:
        if(checkBoutonHover(boutonCar1, mousePos)):
          game.player.initType(1)
          game.STATE = GameState.PLAY
          mixer.music.load("../nsipoo/Assets/sounds/music.mp3")
          mixer.music.play(-1, 57, 5)

        if(checkBoutonHover(boutonCar2, mousePos)):
          game.player.initType(2)
          game.STATE = GameState.PLAY
          mixer.music.load("../nsipoo/Assets/sounds/music.mp3")
          mixer.music.play(-1, 57, 5)

        if(checkBoutonHover(boutonCar3, mousePos)):
          game.player.initType(3)
          game.STATE = GameState.PLAY
          mixer.music.load("../nsipoo/Assets/sounds/music.mp3")
          mixer.music.play(-1, 57, 5)

        if(checkBoutonHover(boutonCar4, mousePos)):
          game.player.initType(4)
          game.STATE = GameState.PLAY
          mixer.music.load("../nsipoo/Assets/sounds/music.mp3")
          mixer.music.play(-1, 57, 5)

        if(checkBoutonHover(boutonCar5, mousePos)):
          game.player.initType(5)
          game.STATE = GameState.PLAY
          mixer.music.load("../nsipoo/Assets/sounds/music.mp3")
          mixer.music.play(-1, 57, 5)

        if(checkBoutonHover(boutonQuit, mousePos)):
          game.STATE = GameState.QUIT

        if(checkBoutonHover(boutonMENU, mousePos)):
          main()

        if(checkBoutonHover(boutonQuitDeath, mousePos)):
          game.STATE = GameState.QUIT


    if game.STATE == GameState.QUIT: pygame.quit()
    if game.STATE == GameState.MENU: menu(game, mousePos)
    if game.STATE == GameState.DEAD: 
      menu(game, mousePos)
      pygame.mixer.music.stop()

    if game.STATE == GameState.PLAY:
        clock.tick(120)
        game.Deathcount = 0
        keyListener = pygame.key.get_pressed()
        if(keyListener[K_k]): drawHitBox = True

        game.play(window, keyListener) 
        display.flip()

        if game.isOver: game.STATE = GameState.DEAD

def menu(game, mousePos):
    window.blit(menuImage, (0,0))

    if game.Deathcount == 0:
        window.blit(menuImage, (0,0))
        text = mainFont.render("Choose your car", True, whiteColor)
        window.blit(text, (gameWidth / 2 - text.get_width() / 2, gameHeight / 3 - text.get_height()))

        if(checkBoutonHover(boutonCar1, mousePos)):  draw.rect(window, greenColor, boutonCar1)
        window.blit(perso1, boutonCar1)

        if(checkBoutonHover(boutonCar2, mousePos)):  draw.rect(window, greenColor, boutonCar2)
        window.blit(perso2, boutonCar2)

        if(checkBoutonHover(boutonCar3, mousePos)):  draw.rect(window, greenColor, boutonCar3)
        window.blit(perso3, boutonCar3)

        if(checkBoutonHover(boutonCar4, mousePos)):  draw.rect(window, greenColor, boutonCar4)
        window.blit(perso4, boutonCar4)

        if(checkBoutonHover(boutonCar5, mousePos)):  draw.rect(window, greenColor, boutonCar5)
        window.blit(perso5, boutonCar5)

        if(checkBoutonHover(boutonQuit, mousePos)):  draw.rect(window, whiteColor, boutonQuit)
        else: draw.rect(window, redColor, boutonQuit)

        quitText = mainFont.render('Quit', True, blackColor)
        window.blit(quitText, (boutonQuit.x + boutonQuit.width /2 - quitText.get_width()/2, boutonQuit.y + boutonQuit.height /2 - quitText.get_height()/2))

    elif game.Deathcount > 0:

        
        window.blit(deathImage, (0,0))
        text = mainFont.render("Score", True, whiteColor)
        window.blit(text, (gameWidth / 2 - text.get_width() / 2, gameHeight / 2.3 - text.get_height()))


        if(checkBoutonHover(boutonMENU, mousePos)):  draw.rect(window, whiteColor, boutonMENU)
        else: draw.rect(window, redColor, boutonMENU)

        if(checkBoutonHover(boutonQuitDeath, mousePos)):  draw.rect(window, whiteColor, boutonQuitDeath)
        else: draw.rect(window, redColor, boutonQuitDeath)

        playText = mainFont.render('Return to Menu', True, blackColor)
        window.blit(playText, (boutonMENU.x + boutonMENU.width /2 - playText.get_width()/2, boutonMENU.y + boutonMENU.height /2 - playText.get_height()/2))

        quitText = mainFont.render('Quit', True, blackColor)
        window.blit(quitText, (boutonQuitDeath.x + boutonQuitDeath.width /2 - quitText.get_width()/2, boutonQuitDeath.y + boutonQuitDeath.height /2 - quitText.get_height()/2))



        score = mainFont.render(str(game.score.point), True, yellowColor)
        scoreRect = score.get_rect()
        scoreRect.center = (gameWidth / 2, gameHeight / 2 - 20 )
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