import sys

import pygame
from config import Color
from game import Game
from menu import Menu
from endScreen import EndScreen

pygame.init()

game = Game()
menu = Menu("TWO CARS", game.width)
endScreen = EndScreen()

mainWindow = pygame.display.set_mode(
    (max(game.width, menu.width), game.height + menu.height)
)
pygame.display.set_caption("Two Cars")
FPS = 60

clock = pygame.time.Clock()


def draw():
    mainWindow.fill(Color.BLUE)
    menu.draw(mainWindow)   
    game.draw(mainWindow, (0, menu.height))
    if game.gameOver:
        endScreen.draw(mainWindow, pygame.Vector2(0, menu.height))
    pygame.display.update()


def reset():
    game.reset()


def displayEndScreen():
    pass


def main():
    running = True

    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            # checking if the game has been exited
            if event.type == pygame.QUIT:
                running = False
                break
        
        # updating the diplayed score
        menu.score = game.score
        
        # drawing all the elements
        draw()
        
        # handling movements and collisions
        game.handleTrafficMovement()
        game.handleCollisions()
        
        # TODO if the game got over then display the end screen
        # for now this just closes the game
        running = not game.gameOver
        if game.gameOver:
            displayEndScreen()
        
        # handling keyboard inputs
        keys = pygame.key.get_pressed()
        game.handleCarMovement(keys)

        
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()