import pygame

#initialising pygame
pygame.init()

#create the window screen
screen = pygame.display.set_mode((800,600)) 

#Game loop, so that the window stays
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Finding out if X has been pressed and closing the window 
            running = False