# Import pygame
import pygame

# Import random library
import random

# Initializate pygame
pygame.init()

# Window size
SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

# Size variable
SIZE = ( SCREEN_WIDTH, SCREEN_HEIGHT )

# Display the windows
screen = pygame.display.set_mode( SIZE )

# Title
pygame.display.set_caption("Space Invaders @Adakademy")

# Icon
icon = pygame.image.load( "ufo.png" )
pygame.display.set_icon( icon )

# Player
player_img = pygame.image.load( "player_a.png" )
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = pygame.image.load("enemy_a.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 0.1  
enemy_y_change = 30
# Player function
def player(x, y):
    screen.blit( player_img, (x, y))

# Enemy function
def enemy(x, y):
    screen.blit( enemy_img, (x, y))    

# Game loop
running = True
while running:

    # Increase the speed in x
    #player_x += 0.1
    #print( player_x )


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_x_change = -0.5

            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_x_change = 0



    # Background color RGB -> Red, Green, Blue
    RGB = (100, 100, 100)
    screen.fill( RGB )

    # Increment or decrement the x variable
    player_x += player_x_change

    # Player boundaries left
    if player_x <= 0:
        player_x = 0

    # Player boundaries right
    elif player_x >= 736:
        player_x = 736
    
    enemy_x += enemy_x_change 
    if enemy_x >= 736:
        enemy_x_change = -0.1 
        enemy_y += enemy_y_change

    elif enemy_x <= 0:
        enemy_x_change += 0.1 
        enemy_y += enemy_y_change 
    # Call the player function
    player(player_x, player_y)

        # Call the player function
    enemy(enemy_x, enemy_y)

        # Update the window
    pygame.display.update()
