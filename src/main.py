#import all the things

#main function
#parameters: none
    #while true
        #call login function
        #if it returns quit
            #show a message about leaving
            #break
        #else:
            #while true
                #choice is them choosing a button of the action they want to complete
                #if they choose user stuff(to be decided)
                #else if they choose poker
                    #run poker game
                #else if they choose blackjack
                    #run blackjack
                #else if they choose slots
                    #run slots
                #else if they choose exit
                    #message
                    #break

import random as r
import pygame
pygame.init()

screen = pygame.display.set_mode((1320, 960))
clock = pygame.time.Clock()
button_rect = pygame.Rect(150, 100, 100, 50)
font = pygame.font.SysFont('Arial', 12)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT and event.key == pygame.K_F4:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                screen.blit(pygame.image.load("docs/minion_2.jpg"), (100, 100))

