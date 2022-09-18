import pygame as pyg
import random as rnd
import math

# Initialize pygame
pyg.init()

# Set screen size (width,height)
screen = pyg.display.set_mode((800,600))

#Set Title of the window
pyg.display.set_caption('Space Invaders')

#Player
playerimg = pyg.image.load('battleship.png') #load player sprite

#Background
backgroundimg = pyg.image.load('space_background_2_edited.png').convert() #load background

#set position of player sprite
player_x = 370 
player_y = 480
player_x_change = 0
player_y_change = 0
player_speed = 0.5

#Enemy
enemyimg = pyg.image.load('ufo.png') #load enemy sprite
#set position of enemy sprite
enemy_x = rnd.randint(0, 734)
enemy_y = rnd.randint(50, 150)
enemy_x_change = 0.1
enemy_y_change = 0.02


#Bullet
bulletimg = pyg.image.load('minus_32.png')
bullet_x = 0
bul_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 1.2
bullet_state = "ready"
bullet_speed = 0.5

score = 0

#draw the player sprite on the screen
def player(x,y):
    screen.blit(playerimg, (x, y))

#draw the enemy sprite
def enemy(x, y):
    screen.blit(enemyimg, (x, y))

#fire the bullet
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y+10))

#Check if collision occured
def isCollision(enemy_x,enemy_y,bullet_x, bullet_y,state):
    dist = math.sqrt(((enemy_x - bullet_x)**2) + ((enemy_y - bullet_y)**2))
    if dist < 27 and state == "fire":
        return True
    else:
        return False

#Game loop
running = True
while running:
    for event in pyg.event.get(): # Keep the window open unless user presses quit
        if event.type == pyg.QUIT:
            running = False
                            
        if event.type == pyg.KEYDOWN:  # if keystroke is pressed and matches arrow keys, move the sprite
            if event.key == pyg.K_LEFT:
                player_x_change = -player_speed
            if event.key == pyg.K_RIGHT:
                player_x_change = player_speed
#           if event.key == pyg.K_UP:
#               player_y_change = -player_speed
#          if event.key == pyg.K_DOWN:
#                player_y_change = player_speed
            if event.key == pyg.K_SPACE:
                if bullet_state == "ready":
                    bul_x = player_x
                    fire_bullet(bul_x, bullet_y)
        if event.type == pyg.KEYUP:
            if event.key == pyg.K_LEFT or event.key == pyg.K_RIGHT:
                player_x_change = 0
            if event.key == pyg.K_UP or event.key == pyg.K_DOWN:
                player_y_change = 0

    screen.fill((0,0,0)) #fill the screen with colour (R,G,B)
    screen.blit(backgroundimg, (0,0)) #display background image

    # change the position by speed to move the sprite
    player_x += player_x_change
    player_y += player_y_change

    # keep the sprite within the window boundaries
    if player_x < 0:
        player_x = 0
    elif player_x > 736:
        player_x = 736
#    if player_y < 0:
#        player_y = 0
#    elif player_y > 536:
#        player_y = 536

    enemy_x += enemy_x_change
    enemy_y += enemy_y_change

    if enemy_x < 0:
        enemy_x = 0
        enemy_x_change = -enemy_x_change
        enemy_y += enemy_y_change
    elif enemy_x > 736:
        enemy_x = 736
        enemy_x_change = -enemy_x_change
        enemy_y += enemy_y_change
    
    #Bullet movement
    if bullet_y <= -5:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bul_x, bullet_y)
        bullet_y -= bullet_y_change
    
    #Collision
    if isCollision(enemy_x, enemy_y,bul_x, bullet_y, bullet_state):
        bullet_y = 480
        bullet_state = "ready"
        score += 1
        enemy_x = rnd.randint(0, 734)
        enemy_y = rnd.randint(50, 150)
        print(score)
    
    
    player(player_x, player_y)    
    enemy(enemy_x, enemy_y)

    pyg.display.update()