import pygame


class Color:
    
    WHITE: pygame.Color =      pygame.Color(255, 255, 255)
    BLACK: pygame.Color =      pygame.Color(0, 0, 0)
    GRAY_LIGHT: pygame.Color = pygame.Color(192, 192, 192)
    GRAY_DARK: pygame.Color =  pygame.Color(32, 32, 32)
    RED: pygame.Color =        pygame.Color(255, 36, 36)
    RED_LIGHT: pygame.Color =  pygame.Color(255, 107, 107)
    RED_DARK: pygame.Color =   pygame.Color(194, 10, 10)
    BLUE: pygame.Color =       pygame.Color(33, 157, 252)
    BLUE_LIGHT: pygame.Color = pygame.Color(102, 173, 255)
    BLUE_DARK: pygame.Color =  pygame.Color(7, 87, 179)
    
    
class Dimension:
    
    LANE_HEIGHT: int = 700
    LANE_WIDTH: int = 100
    LANE_NUM = 4
    LINE_WIDTH = 4
    BORDER_RADIUS = 10
    TRAFFIC_HEIGHT = 40
    TRAFFIC_WIDTH = 35
    TRAFFIC_START_SPEED = 5
    TRAFFIC_START_ACCELERATION = 0.001
    TRAFFIC_COLLECTIBILITY = (True, False, False, False)
    CAR_WIDTH = 40
    CAR_HEIGHT = 70
    CAR_BOTTOM_PADDING = 50
    CAR_START_SPEEDX = TRAFFIC_START_SPEED - 1
    CAR_START_ACCELERATIONX = TRAFFIC_START_ACCELERATION
    CAR_MAX_SPEED_LIMIT = 6
    GAME_WIDTH = LANE_NUM * LANE_WIDTH + (LANE_NUM + 1) * LINE_WIDTH
    GAME_HEIGHT = LANE_HEIGHT
    MENU_WIDTH = GAME_WIDTH
    MENU_HEIGHT = 80
    MENU_TITLE_TEXT = "TWO CARS"
    MENU_TITLE_HEIGHT = int(MENU_HEIGHT / 1.5)
    WINDOW_WIDTH = max(MENU_WIDTH, GAME_WIDTH)
    WINDOW_HEIGHT = MENU_HEIGHT + GAME_HEIGHT

    @staticmethod
    def getLaneXfromLaneNum(laneNum: int) -> float:
        assert laneNum in range(4), "invalid lane number"
        return laneNum * Dimension.LANE_WIDTH + (laneNum + 1) * Dimension.LINE_WIDTH