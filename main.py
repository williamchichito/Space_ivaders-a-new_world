# Importing pygame 
from asyncio import windows_events
from turtle import distance
import pygame 
import random 
import math
#intalizatin pygame 
pygame.init() 

# wowndow slize 

screen_width = 800 
screen_height = 600 

# size variable 
size = (screen_width, screen_height)  

# Title 
pygame.display.set_caption("Sapace Invaders by willyWonka")

# icon
icon = pygame.image.load("./main.pygame/enemigo.png")
pygame.display.set_icon(icon)

# background img
background = pygame.image.load("./main.pygame/un-espacio-con-muchas-estrellas-y-planetas--y-sin-humanos-447174450.png")

screen = pygame.display.set_mode(size)
  

# bala 
bala_x = 370
bala_y = 480
bala_image = pygame.image.load("./main.pygame/bala.png")  
bala_img_tr = pygame.transform.scale(bala_image,(64,64))
bala_x_change = 0
bala_y_change = 10
bala_state = True

def fire(x,y): 
    global bala_state 
    bala_state = False
    screen.blit(bala_img_tr,(x,y))
# collision 

def is_collision (b_x, b_y, e_x, e_y): 
   distance = math.sqrt((e_x - b_x)**2 + (e_y - b_y)**2) 
   if distance < 27: 
     return True 
   else: 
     return False

   # PLAYER FUNTION 

player_x = 370
player_y = 480
player_image = pygame.image.load("./main.pygame/astronave.png") 
player_x_change = 0
 
def player(x,y): 
    screen.blit(player_image,(x,y))
 
 #enemy

enemy_x = random.randint(0,300)
enemy_y =  random.randint(0,300)
enemy_image = pygame.image.load("./main.pygame/enemigo.png") 
enemy_img_tr = pygame.transform.scale(enemy_image,(64,64))
enemy_x_change = 4
enemy_y_change = 40
 
def enemy(x,y): 
    screen.blit(enemy_img_tr,(x,y))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            



    # surperficie                                                                                         
running = True
clock = pygame.time.Clock()
while running: 
    for event  in pygame.event.get(): 
        if event.type == pygame.QUIT: 
         running = False 
        # keyboard inputs
        if event.type == pygame.KEYDOWN: 
           
           if event.key == pygame.K_LEFT:
            player_x_change = -1.5


           if event.key == pygame.K_RIGHT:
            player_x_change = 1.5 
          
           if event.key == pygame.K_SPACE and bala_state == True: 
            bala_x =  player_x
            fire(bala_x,bala_y)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                player_x_change = -0


            if event.key == pygame.K_RIGHT:
                player_x_change = 0

        
        
    
#blit of the background 
    screen.blit(background, (0,0)) 
# bala movements 

 
    if bala_state == False: 
        fire(bala_x,bala_y) 
        bala_y -= bala_y_change
       
    if bala_y <= 0: 
      bala_y = 480 
      bala_state = True
    collision = is_collision(bala_x, bala_y, enemy_x, enemy_y)
    if collision: 
        bala_y = 480 
        bala_state = True 
        enemy_x = random.randint(0,300)
        enemy_y =  random.randint(0,300)

#player movements
    
    player_x += player_x_change
    
    player(player_x,player_y)

    if player_x <= 0:
       player_x = 0
    
    elif player_x >= 750: 
       player_x = 750 

# enemy movements

    enemy(enemy_x,enemy_y)
 
    enemy_x += enemy_x_change
    if enemy_x <= 0 : 
        enemy_x_change = 4
        enemy_y += enemy_y_change

    elif enemy_x >= 736 : 
        enemy_x_change = -4
        enemy_y += enemy_y_change 


   

    # bala movements 

    pygame.display.flip() 

pygame.quit() 




     