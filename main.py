
# importing libraries
import pygame
import time
import random
 
snake_speed = 15
 
# Window size
window_x = 720
window_y = 480
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('BoSTEM Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [window_x//2, window_y//2]
 
# defining first block of snake's body
snake_body = [  [window_x//2, window_y//2],
            ]

# getting random fruit positions
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True
 
# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction