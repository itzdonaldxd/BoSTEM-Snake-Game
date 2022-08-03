
# importing libraries
import pygame
import time
import random
 
snake_speed = 15
snake_size = 20
fruit_size = 10
 
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

# # Main Function

while True:
    
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            # print(change_to)
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two directions
    # simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= snake_size
    if direction == 'DOWN':
        snake_position[1] += snake_size
    if direction == 'LEFT':
        snake_position[0] -= snake_size
    if direction == 'RIGHT':
        snake_position[0] += snake_size
    
    # Insert the new snake position
    snake_body.insert(0, list(snake_position))
    
    # Remove the old snake position
    snake_body.pop()
    
    # Erase the old snake position from the screen
    game_window.fill(black)
 
	# Drawing the snake at the newest position
    for pos in snake_body:
        pygame.draw.rect(game_window, green, 
                         pygame.Rect(pos[0], pos[1], snake_size, snake_size))
    
    # Refresh game screen
    pygame.display.update()
    
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)




