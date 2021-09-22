import pygame
import random
import os
import math
from pygame import mixer
import time

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def start():
    global play
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center Pygame window
    # initialising pygame
    pygame.mixer.pre_init()
    pygame.init()

    # create the window screen
    screen = pygame.display.set_mode((800, 600))

    # background image
    background = pygame.image.load('./assets/bg.png')

    # background sound
    background_music = mixer.music.load('./sounds/Intergalactic Odyssey.wav')
    mixer.music.play(-1)

    #Title and Icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('./assets/Gameicon.png')  # icon added from flaticon
    pygame.display.set_icon(icon)

    # player
    playerImg = pygame.image.load('./assets/spaceship.png')
    playerX = 370
    playerY = 480
    playerX_change = 0

    # enemy
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = random.randint(5, 10)

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('./assets/alien.png'))
        enemyX.append(random.randint(0, 735))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)

    # Bullet
    bulletImg = [pygame.image.load('./assets/bullet.png')]*10
    bulletX = [0]*10
    bulletY = [480]*10
    bulletX_change = 0
    bulletY_change = [10]*10

    # ready means can't see the bullet on the screen and fire means bullet is currently moving.
    bullet_state = ["ready"]*10
    bullet_no = 0

    # Score
    score_value = 0
    font = pygame.font.Font('./assets/ka1.ttf', 28)

    textX = 10
    textY = 10

    # GameOver
    over_font = pygame.font.Font('./assets/ka1.ttf', 64)
    play_font = pygame.font.Font('./assets/ka1.ttf', 32)



    def showScore(x, y):
        score = font.render("Score : " + str(score_value), True, (0, 255, 0))
        screen.blit(score, (x, y))


    def gameOver():
        game_over = over_font.render("GAME OVER", True, (255, 50, 0))
        restart_game = play_font.render("Press r to restart", True, (55, 250, 0))
        quit_game = play_font.render("Press q to quit", True, (55, 250, 0))
        screen.blit(game_over, (150, 200))
        screen.blit(restart_game, (150, 300))
        screen.blit(quit_game, (150, 350))


    def player(x, y):
        screen.blit(playerImg, (x, y))  # Draw the player according to co-ordinates


    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))


    def fireBullet(x, y, id):
        global bullet_no
        bullet_state[id] = 'fire'
        screen.blit(bulletImg[id], (x + 16, y + 10))


    def hasCollided(enemyX, enemyY, bulletX, bulletY):
        dis = math.hypot((bulletX-enemyX), (bulletY-enemyY))  # Distance formula
        if dis < 27:
            explode_sound = mixer.Sound('sounds/expo.wav')
            mixer.Channel(0).play(explode_sound)
            return True
        else:
            return False


# Game loop, so that the window stays
    running = True
    while running:

        # RGB value
        screen.fill((20, 20, 30))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Finding out if X has been pressed and closing the window
                running = False
            # if keystroke is pressed,check whether it's right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state[bullet_no] == 'ready':
                        bullet_sound = mixer.Sound('sounds/lasergun.wav')
                        mixer.Channel(1).play(bullet_sound)
                        bulletX[bullet_no] = playerX
                        fireBullet(bulletX[bullet_no],
                                   bulletY[bullet_no], bullet_no)
                        if bullet_no == 9:
                            bullet_no = 0
                        else:
                            bullet_no += 1
                if event.key == pygame.K_r:
                    running = False
                elif event.key == pygame.K_q:
                    running = False
                    play = 0
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change

        # Condition for bounds
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy movement
        for i in range(num_of_enemies):
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                gameOver()  # game over
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]
            # collision
            for k in range(10):
                collision = hasCollided(
                    enemyX[i], enemyY[i], bulletX[k], bulletY[k])
                if collision:
                    bulletY[k] = 480
                    bullet_state[k] = 'ready'
                    score_value += 1
                    enemyX[i] = random.randint(0, 735)
                    enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        for i in range(10):
            if bulletY[i] <= 0:
                bulletY[i] = 480
                bullet_state[i] = 'ready'
            if bullet_state[i] == 'fire':
                fireBullet(bulletX[i], bulletY[i], i)
                bulletY[i] -= bulletY_change[i]

        player(playerX, playerY)
        showScore(textX, textY)
        pygame.display.update()  # update needed to change the colour to white


play = 1

while play:
    time.sleep(1)
    start()
