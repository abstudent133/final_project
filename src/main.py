#import all the things
from blackjack import*
from gift_shop import*
from login import*
from poker import*
from slots import*
from view_profile import*
from work import*

#main function
def main():
#parameters: none
    #while true
    while True:
        #call login function
        pass
        #if it returns quit
            #show a message about leaving
            #break
        #else:
            #while true
                #choice is them choosing a button of the action they want to complete
                #if they choose edit profile(shop)
                    #call shop function
                #else if they choose poker
                    #run poker game
                #else if they choose blackjack
                    #run blackjack
                #else if they choose slots
                    #run slots
                #else if they choose to work
                    #call work function
                #else if they choose exit
                    #message
                    #break

import random as r
import pygame
pygame.init()

def draw_face():

    screen = pygame.display.set_mode((1320, 960))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 12)
    button_img = pygame.image.load("docs/minion_2.jpg").convert_alpha()
    button_rect = button_img.get_rect()
    # screen.blit(button_img, button_rect)

    drawing = False
    radius = 3
    current_stroke = []
    strokes = []

    def draw_line(surface, color, points, radius):
        if len(points) > 1:
            pygame.draw.lines(surface, color, False, points, radius * 2)

    def redraw(surface):
        surface.fill("black")
        for stroke in strokes:
            draw_line(surface, "white", stroke, radius)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and pygame.KMOD_LCTRL:
                    if strokes:
                        strokes.pop()
                        redraw(screen)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and pygame.KMOD_LSHIFT:
                    pygame.image.save(screen, "docs/face.jpg")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                current_stroke = [event.pos]

            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                if current_stroke:
                    strokes.append(current_stroke)
                current_stroke = []

            elif event.type == pygame.MOUSEMOTION and drawing:
                current_stroke.append(event.pos)

        redraw(screen)

        if current_stroke:
            draw_line(screen, "white", current_stroke, radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

draw_face()