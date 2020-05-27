import pygame,random,os

os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center Pygame window
#initialising pygame
pygame.init()

#create the window screen
screen = pygame.display.set_mode((800,600)) 

#background image
background = pygame.image.load('assets/bg.png')

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
enemyX_change = 4
enemyY_change = 40

#Bullet
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = 0 
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready" # read means can't see the bullet on the screen and fire means bullet is currently moving.


def player(x,y):
    screen.blit(playerImg,(x,y))   #Draw the player according to co-ordinates


def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fireBullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg ,(x + 16, y +10))


#Game loop, so that the window stays
running = True
while running:
    #RGB value
    screen.fill((20 ,20, 30))  
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Finding out if X has been pressed and closing the window 
            running = False
        #if keystroke is pressed,check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fireBullet(bulletX,bulletY)    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0                
    
    playerX += playerX_change

    #Condition for bounds
    if playerX<=0:
        playerX=0
    elif playerX >= 736:
        playerX = 736

    if enemyX<=0:
        enemyX_change=4
        enemyY+=enemyY_change
    elif enemyX >= 736:
        enemyX_change=-4    
        enemyY+=enemyY_change
    enemyX+=enemyX_change    

    if bulletY<=0:
            bulletY=480
            bullet_state='ready'
    if bullet_state is 'fire':
        fireBullet(bulletX,bulletY)
        bulletY-=bulletY_change
        

    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update() #update needed to change the colour to white        