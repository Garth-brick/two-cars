import pygame
from config import Color, Dimension


class Car:
    WIDTH = Dimension.CAR_WIDTH
    HEIGHT = Dimension.CAR_HEIGHT
    LANE_SWITCH = {0:1, 1:0, 2:3, 3:2}
    COLOR_MAP = {0:Color.RED, 1:Color.BLUE}
    HIGHLIGHT_COLOR_MAP = {0:Color.RED_LIGHT, 1:Color.BLUE_LIGHT}
    START_MAX_SPEED = Dimension.CAR_START_SPEEDX
    CAR_ACCELERATIONX = Dimension.CAR_START_ACCELERATIONX


    def __init__(self, laneNum: int, ID: int, width: int = WIDTH, height: int = HEIGHT) -> None:
        assert laneNum in range(4)
        assert ID in range(2)
        
        self.laneNum = laneNum
        self.width = width
        self.height = height
        self.ID = ID
        self.color = Car.COLOR_MAP[ID]
        self.colorHighlight = Car.HIGHLIGHT_COLOR_MAP[ID]
        self.x = Dimension.getLaneXfromLaneNum(laneNum) + Dimension.LANE_WIDTH / 2 - width / 2
        self.y = Dimension.LANE_HEIGHT - Dimension.CAR_BOTTOM_PADDING - height
        self.inTransition = False
        self.speedX = 0
        self.destinationX = self.x
        self.maxSpeed = Car.START_MAX_SPEED


    def switchLanes(self):
        if not self.inTransition:
            self.inTransition = True
            self.laneNum = Car.LANE_SWITCH[self.laneNum]
            self.destinationX = self.getCarXfromLaneNum(self.laneNum)
            self.transitionCarX()


    def transitionCarX(self):
        if self.destinationX == self.x:
            self.speedX = 0
            self.inTransition = False
        if self.destinationX > self.x:
            self.speedX = min(self.destinationX - self.x, self.maxSpeed)
        if self.destinationX < self.x:
            self.speedX = max(self.destinationX - self.x, -self.maxSpeed)
        self.x += self.speedX


    def getCarXfromLaneNum(self, laneNum: int) -> float:
        return Dimension.getLaneXfromLaneNum(self.laneNum) + Dimension.LANE_WIDTH / 2 - self.width / 2


    def draw(self, gameScreen: pygame.Surface) -> None:
        
        # updating the speed by the amount of acceleration
        if self.maxSpeed <= Dimension.CAR_MAX_SPEED_LIMIT:
            self.maxSpeed += Car.CAR_ACCELERATIONX
        
        # drawing the body of the car
        pygame.draw.rect(
            gameScreen,
            self.color,
            (self.x, self.y, self.width, self.height),
            0,
            Dimension.BORDER_RADIUS
        )
        # drawing the border highlight
        pygame.draw.rect(
            gameScreen,
            self.colorHighlight,
            (self.x, self.y, self.width, self.height),
            Dimension.LINE_WIDTH,
            Dimension.BORDER_RADIUS
        )


    def isInside(self, point: pygame.math.Vector2) -> bool:
        if (self.x <= point.x <= self.x + self.width and
            self.y <= point.y <= self.y + self.height):
            return True
        return False