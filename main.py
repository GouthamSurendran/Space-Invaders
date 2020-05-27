import pygame
import random

#initialising pygame
pygame.init()

#create the window screen
screen = pygame.display.set_mode((800,600)) 

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/Gameicon.png') #icon added from flaticon
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('assets/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = pygame.image.load('assets/alien.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0


def player(x,y):
    screen.blit(playerImg,(x,y))   #Draw the player according to co-ordinates


def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#Game loop, so that the window stays
running = True
while running:
    #RGB value
    screen.fill((20 ,20, 30))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Finding out if X has been pressed and closing the window 
            running = False
        #if keystroke is pressed,check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0
    
    playerX += playerX_change

    #Condition for bounds
    if playerX<=0:
        playerX=0
    elif playerX >= 736:
        playerX = 736

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update() #update needed to change the colour to white        