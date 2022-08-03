
# importing libraries
import pygame
import time
import random
 
snake_speed = 15
snake_size = 10
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
fruit_spawn = False
 
# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

# Function to determine if two blocks overlap
def collision_detected(block_pos_1, block_pos_2):
    
    # Returns true if x,y coords overlap, otherwise false
    return block_pos_1[0] == block_pos_2[0] and block_pos_1[1] == block_pos_2[1]


# Game over function: Show text saying Game Over
def game_over():
    # Create font obj
    my_font = pygame.font.SysFont('times new roman', 50)
    
	# creating a text surface on which text will be drawn
    game_over_surface = my_font.render('Game Over', True, red)
    
	# create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x//2, window_y//4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 3 seconds we will quit the program
    time.sleep(3)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
    
    

# Main Function

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
	# Snake body growing mechanism, if fruit and snake collide, add one to the body length
    snake_body.insert(0, list(snake_position))
    if collision_detected(snake_position, fruit_position):
        fruit_spawn = True
    else:
        # Remove the old snake position
        snake_body.pop()
        
    # If a fruit was eaten, spawn a new fruit
    if fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    
    fruit_spawn = False 
    
    # Erase the old snake position from the screen
    game_window.fill(black)
 
	# Drawing the snake at the newest position
    for pos in snake_body:
        pygame.draw.rect(game_window, green, 
                         pygame.Rect(pos[0], pos[1], snake_size, snake_size))
        
    pygame.draw.rect(game_window, white,
                     pygame.Rect(fruit_position[0], fruit_position[1], fruit_size, fruit_size))
    
    # Game Over Conditions
    
    # If snake goes outside game window
    if snake_position[0] < 0 or snake_position[0] > window_x-snake_size: # x boundaries
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-snake_size: # y boundaries
        game_over()
    
    # If snake eats itself
    for block in snake_body[1:]:
        if collision_detected(snake_position, block):
            game_over()
    
    
    
    # Refresh game screen
    pygame.display.update()
    
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)




