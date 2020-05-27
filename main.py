import pygame

#initialising pygame
pygame.init()

#create the window screen
screen = pygame.display.set_mode((800,600)) 

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Gameicon.png') #icon added from flaticon
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480

def player(x,y):
    screen.blit(playerImg,(x,y))   #Draw the player according to co-ordinates

#Game loop, so that the window stays
running = True
while running:
    #RGB value
    screen.fill((0 ,0, 0))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Finding out if X has been pressed and closing the window 
            running = False
        #if keystroke is pressed,check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                playerX-=5
            if event.key == pygame.K_RIGHT:
                playerX+=5

    player(playerX,playerY)
    pygame.display.update() #update needed to change the colour to white        