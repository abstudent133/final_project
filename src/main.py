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
button_rect = pygame.Rect(150, 100, 100, 50)
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 12)

cookies = 0

minions = ["docs\minion.jpg", "docs\minion_3.jpg", "docs\minion_2.jpg", "docs\minion_1.jpg"]



running = True
while running:
    minion = pygame.image.load(r.choice(minions))
    gouda = r.randint(0, 1000)
    cheddar = r.randint(0, 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                    text_surface = font.render('I am placing blocks and stuff \'cause I\'m in fluffing minecraft', True, (255, 255, 255))
    
                    screen.blit(minion, (gouda, cheddar))

                    pygame.display.flip()
                    clock.tick(60)

            

    pygame.draw.rect(screen, (255, 0, 0), button_rect)
    pygame.display.flip()

