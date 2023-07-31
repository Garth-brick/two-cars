import random

import pygame
from car import Car, Dimension
from config import Color
from traffic import Traffic


class Game:
    LINE_WIDTH: int = Dimension.LINE_WIDTH
    LANE_NUM: int = Dimension.LANE_NUM
    LANE_WIDTH: int = Dimension.LANE_WIDTH
    WIDTH: int = Dimension.GAME_WIDTH
    HEIGHT: int = Dimension.LANE_HEIGHT
    
    
    def __init__(self, width: int = WIDTH, height: int = HEIGHT):
        self.width = width
        self.height = height
        self.gameWindow = pygame.Surface((width, height))
        self.font = pygame.font.SysFont("fonts\\Roboto-Medium.ttf", int(height / 10))
        self.trafficList: list[Traffic] = []
        self.initialiseTrafficList()
        self.carList: list[Car] = []
        self.initialiseCarList()
        self.gameOver = False
        self.score = 0
        
        
    def initialiseTrafficList(self):
        for laneNum in range(4):
            laneX = Dimension.getLaneXfromLaneNum(laneNum)
            startX = laneX + Game.LANE_WIDTH / 2 - Dimension.TRAFFIC_WIDTH / 2
            startY = -Dimension.TRAFFIC_HEIGHT if laneNum % 2 else -Dimension.TRAFFIC_HEIGHT - self.height / 2
            self.trafficList.append(
                Traffic(
                    laneNum, 
                    random.choice((False, True)), 
                    startX,
                    startY
                )
            )


    def initialiseCarList(self):
        for i in range(2):
            self.carList.append(Car(
                i*2,
                i,
            ))
        
    
    def drawLines(self) -> None:
        for i in range(5):
            if i == 0 or i == 2 or i == 4:
                color = Color.GRAY_LIGHT
            else:
                color = Color.GRAY_DARK
            pygame.draw.rect(
                self.gameWindow,
                color,
                (i * (Game.LINE_WIDTH + Game.LANE_WIDTH), 0, Game.LINE_WIDTH, self.height)
            )


    def drawObstacles(self) -> None:
        for traffic in self.trafficList:
            traffic.draw(self.gameWindow)


    def handleTrafficMovement(self) -> None:
        for traffic in self.trafficList:
            traffic.moveDown()
            if traffic.y >= self.height:
                traffic.reset()

    
    def drawCars(self) -> None:
        for car in self.carList:
            car.draw(self.gameWindow)

    
    def handleCarMovement(self, keys: pygame.key.ScancodeWrapper) -> None:
        if keys[pygame.K_LEFT]:
            self.carList[0].switchLanes()
        if keys[pygame.K_RIGHT]:
            self.carList[1].switchLanes()
        for car in self.carList:
            if car.inTransition:
                car.transitionCarX()
    
    @staticmethod
    def checkOverlap(car: Car, traffic: Traffic):
        vertices = traffic.getVertices()
        for vertex in vertices:
            if car.isInside(vertex):
                return True
        return False
    
    # returns True if no collectable missed and no obstacle hit
    def handleCollisions(self) -> None:
        if self.gameOver:
            return
        for car in self.carList:
            for traffic in self.trafficList:
                if not traffic.isVisible:
                    continue
                overlaps = self.checkOverlap(car, traffic)
                if overlaps and traffic.isCollectable:
                    self.score += 1
                    traffic.isVisible = False
                if (overlaps and not traffic.isCollectable or
                    traffic.isCollectable and traffic.y > car.y + car.height):
                    traffic.color = Color.GRAY_LIGHT
                    self.gameOver = True

    
    def draw(self, mainWindow: pygame.Surface, position: tuple[float, float] = (0, 0)) -> None:
        if self.gameOver:
            return
        self.gameWindow.fill(Color.BLACK)
        self.drawLines()
        self.drawObstacles()
        self.drawCars()
        mainWindow.blit(self.gameWindow, position)
        
    def reset(self):
        self.trafficList.clear()
        self.initialiseTrafficList()
        self.carList.clear()
        self.initialiseCarList()
        self.score = 0
        self.gameOver = False
    