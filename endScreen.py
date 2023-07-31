import pygame
from config import Color, Dimension


""" TODO
- Make the endScreen appear when the game gets over
- Display a the top 3 highscores, the current score (maybe also the time taken and the distance travelled)
- Keep a button for restarting the game
- 
"""


class EndScreen:
    
    def __init__(self):
        self.endScreen = pygame.Surface((Dimension.GAME_WIDTH, Dimension.GAME_HEIGHT))
    
    def draw(self, mainWindow: pygame.Surface, position: pygame.Vector2):
        self.endScreen.fill(Color.BLACK)
        