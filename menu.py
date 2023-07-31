from config import Color, Dimension
import pygame


class Menu:
    WIDTH: int = Dimension.MENU_WIDTH
    HEIGHT: int = Dimension.MENU_HEIGHT
    TITLE_TEXT: str = "TWO CARS"
    
    def __init__(self, titleText: str = TITLE_TEXT, width: int = WIDTH, height: int = HEIGHT, score: int = 0) -> None:
        self.width: int = width
        self.height: int = height
        self.titleText: str = titleText
        self.titleFont = pygame.font.Font(r"fonts\NEONLEDLight.otf", int(height / 1.5))
        self.statsFont = pygame.font.SysFont("Consolas", int(height / 1.5))
        self.menuWindow: pygame.Surface = pygame.Surface((width, height))
        self.titleSurface: pygame.Surface = self.titleFont.render(self.titleText, True, Color.WHITE)
        self.score: int = score
        self.gameOver = False
        
    
    def draw(self, mainWindow: pygame.Surface, position: tuple[float, float] = (0, 0)) -> None:
        
        # filling the menu with black
        self.menuWindow.fill(Color.BLACK)
        
        if self.gameOver:
            self.endScreen(mainWindow)
            return
        
        # drawing the title
        padding = self.height / 2 - self.titleSurface.get_height() / 2
        self.menuWindow.blit(
            self.titleSurface, 
            (padding, padding)
        )
        
        # drawing the score
        scoreText = self.statsFont.render(str(self.score), True, Color.WHITE)
        self.menuWindow.blit(
            scoreText,
            (self.menuWindow.get_width() - padding - scoreText.get_width(), self.menuWindow.get_height() / 2 - scoreText.get_height() / 2)
        )
        
        # blit the chnages onto the mainwindow
        mainWindow.blit(self.menuWindow, position)
        
    
    def endScreen(self, mainWindow: pygame.Surface):
        pass
        