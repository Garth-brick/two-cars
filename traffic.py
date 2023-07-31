import random

import pygame
from config import Color, Dimension


class Traffic():
    WIDTH = Dimension.TRAFFIC_WIDTH
    HEIGHT = WIDTH
    SPEED = Dimension.TRAFFIC_START_SPEED
    ACCELERATION = Dimension.TRAFFIC_START_ACCELERATION
    LANE_WIDTH = Dimension.LANE_WIDTH
    LINE_WIDTH = Dimension.LINE_WIDTH
    BORDER_RADIUS = Dimension.BORDER_RADIUS
    COLLECTIBILITY = Dimension.TRAFFIC_COLLECTIBILITY


    def __init__(self, laneNum: int, isCollectable: bool, startX: float, startY: float, width: int = WIDTH, height: int = HEIGHT, laneWidth: int = LANE_WIDTH, speed: float = SPEED, acceleration: float = ACCELERATION):
        assert laneNum in range(4), "invalid obstacle lane number"
        assert width in range(0, laneWidth), "invalid obstacle width"
        assert height in range(0, laneWidth), "invalid obstacle height"
        assert laneWidth > 0, "invalid obstacle lane weight"
        
        self.isCollectable = isCollectable
        self.width = width
        self.height = height
        self.laneWidth = laneWidth
        self.laneNum = laneNum
        self.speed = speed
        self.acceleration = acceleration
        self.x = startX
        self.y = startY
        self.isVisible = True
        if laneNum in range(0, 2):
            self.color = Color.RED
        else:
            self.color = Color.BLUE


    def moveDown(self):
        self.y += self.speed
        self.speed += self.acceleration


    def reset(self) -> None:
        self.isVisible = True
        self.y = -self.height + random.randrange(-Dimension.TRAFFIC_HEIGHT // 4, Dimension.TRAFFIC_HEIGHT // 4)
        if self.laneNum <= 1:
            self.laneNum = random.choice((0, 1))
        else:
            self.laneNum = random.choice((2, 3))
        self.isCollectable = random.choice(Traffic.COLLECTIBILITY)


    def drawCollectable(self, gameWindow: pygame.Surface) -> None:
        # drawing the base circle 
        pygame.draw.circle(
            gameWindow,
            self.color,
            (self.x + self.width / 2, self.y + self.height / 2),
            self.height / 2
        )
        
        # drawing the inner circular highlight
        pygame.draw.circle(
            gameWindow,
            Color.WHITE,
            (self.x + self.width / 2, self.y + self.height / 2),
            self.height / 4,
            Traffic.LINE_WIDTH
        )
        
    
    def drawObstacle(self, gameWindow: pygame.Surface) -> None:
        # drawing the base rectangle
        pygame.draw.rect(
            gameWindow,
            self.color,
            (self.x, self.y, self.width, self.height),
            0,
            Traffic.BORDER_RADIUS
        )
        
        # drawing the inner rectangular highlight rectanngle
        pygame.draw.rect(
            gameWindow,
            Color.WHITE,
            (self.x + self.width / 4, self.y + self.height / 4, self.width / 2, self.height / 2),
            Traffic.LINE_WIDTH
        )


    def draw(self, gameWindow: pygame.Surface):
        if not self.isVisible:
            return
        if self.isCollectable:
            self.drawCollectable(gameWindow)
        else:
            self.drawObstacle(gameWindow)
            
            
    def getVerticesOfSquare(self) -> list[pygame.math.Vector2]:
        return [
            pygame.math.Vector2(self.x, self.y),
            pygame.math.Vector2(self.x, self.y + self.height),
            pygame.math.Vector2(self.x + self.width, self.y),
            pygame.math.Vector2(self.x + self.width, self.y + self.height),
        ]
            
    
    def getVerticesOfCircle(self) -> list[pygame.math.Vector2]:
        radius = pygame.math.Vector2(self.width / 2, 0)
        centre = pygame.math.Vector2(self.x + self.width / 2, self.y + self.height / 2)
        result: list[pygame.math.Vector2] = []
        vertices = 8
        deltaDegrees = 360 // vertices
        for _ in range(vertices):
            result.append(centre + radius)
            radius = radius.rotate(deltaDegrees)
        return result
    
            
    def getVertices(self) -> list[pygame.math.Vector2]:
        if self.isCollectable:
            return self.getVerticesOfCircle()
        return self.getVerticesOfSquare()