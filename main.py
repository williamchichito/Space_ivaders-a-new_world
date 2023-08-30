# Importing pygame 
from asyncio import windows_events
from turtle import distance
import pygame 
import random 
import math 
import os 

from pygame import mixer
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
# Backgraiund sounds 
mixer.music.load("./main.pygame/ruta.wav") 
mixer.music.play( -1 )
   
# background img
background = pygame.image.load("./main.pygame/un-espacio-con-muchas-estrellas-y-planetas--y-sin-humanos-447174450.png")

screen = pygame.display.set_mode(size) 
# score
score_font = pygame.font.Font("main.pygame\AQUATIC.ttf", 32)
  
# variable score

score= 0 

# position text in screen 
text_x = 10
text_y= 10 

# game over font 
go_x = 200 
go_y = 250
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
   
def game_over(x,y): 
    go_text = score_font.render("Game over" , True,(255,255,255)) 
    game_over_sounds = mixer.Sound("./main.pygame/game.wav") 
    game_over_sounds.play() 
    go_condicion = False

    screen.blit(go_text, (x,y)) 

def show_score(x,y): 
    score_text =score_font.render("score: "+ str(score),True,(255,255,255) ) 
    screen.blit(score_text, (x,y))
   # PLAYER FUNTION 

player_x = 370
player_y = 480
player_image = pygame.image.load("./main.pygame/astronave.png") 
player_x_change = 0
 
def player(x,y): 
    screen.blit(player_image,(x,y))
 
 #enemy

enemy_x = [ ]
enemy_y =  [ ]
enemy_image = [ ]
enemy_img_tr = [ ]
enemy_x_change = [ ]
enemy_y_change = [ ] 
number_enemies = 8 
 
for item in range(number_enemies): 
   enemy_image.append(pygame.image.load("./main.pygame/pngwing.com.png")) 
   enemy_x.append(random.randint(0,735)) 
   enemy_y.append(random.randint(50,150)) 
   enemy_x_change.append(4) 
   enemy_y_change.append(40)
def enemy(x,y, item ): 
    screen.blit(enemy_image[ item],(x,y))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            



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
                sonido_de_bala = mixer.Sound("./main.pygame/bala.wav")
                sonido_de_bala.play()
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
            

    #player movements
        
    player_x += player_x_change
        
    player(player_x,player_y)

    if player_x <= 0:
            player_x = 0
        
    elif player_x >= 750: 
            player_x = 750 

    # enemy movements 
    for item in range( number_enemies ):
            
            if enemy_y[ item] > 440:
                for j in range (number_enemies) : 
                    enemy_y[j] =2000 
                game_over(go_x,go_y)
                break 

            collision = is_collision(bala_x, bala_y, enemy_x[item], enemy_y[ item])
            if collision: 
                bala_y = 480 
                bala_state = True  
                score += 25
                enemy_x[ item] = random.randint(0,300)
                enemy_y[ item] =  random.randint(0,300)

            
                
            enemy_x[ item] += enemy_x_change[ item]
            if enemy_x[ item] <= 0 : 
                enemy_x_change[ item] = 4
                

            elif enemy_x[item] >= 736 : 
                enemy_x_change[item] = -4 
                enemy_y[item] += enemy_y_change[ item]

            enemy(enemy_x[ item],enemy_y[ item], item)
        

        # bala movements 
    show_score(text_x,text_y)
    pygame.display.flip() 

pygame.quit() 




     