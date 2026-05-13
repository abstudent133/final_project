import pygame
import random
import time
from classes import *

pygame.init()

width, height = 1280, 1020
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("slot machine")

font = pygame.font.Font(None, 30)

symbols = ['egg', 'footprint', 'shell', 'bone', 'comet']
symbol_images = {}

def spin_grid():
    symbols = ['egg', 'footprint', 'shell', 'bone', 'comet']
    return [[random.choice(symbols) for _ in range(3)] for _ in range(3)]

def symbol_multiplier(symbol):
    return {'egg':1, 'footprint':2, 'shell':5, 'bone':10, 'comet':20}.get(symbol, 0)

def get_payout(grid, bet):
    payout = 0

    for row in grid:
        if row[0] == row[1] == row[2]:
            payout += symbol_multiplier(row[0]) * bet

    if grid[0][0] == grid[1][1] == grid[2][2]:
        payout += symbol_multiplier(grid[0][0]) * bet

    if grid[0][2] == grid[1][1] == grid[2][0]:
        payout += symbol_multiplier(grid[0][2]) * bet

    return payout

cell_size = 80
gap = 20
grid_x = 190
grid_y = 335

money = 100
grid = spin_grid()
bet = 10
min_bet = 1
message = None
max_bet = money

for s in symbols:
    img = pygame.image.load(f"docs/slots_icons/{s}.png").convert_alpha()
    img = pygame.transform.scale(img, (cell_size, cell_size))
    symbol_images[s] = img

def draw():
        screen.blit(bg, (0, 0))

        
        for r in range(3):
            for c in range(3):
                symbol = grid[r][c]

                x = (grid_x + c * (cell_size + gap)) * 2
                y = (grid_y + r * (cell_size + gap))

                screen.blit(symbol_images[symbol], (x, y))

        
        money_text = font.render(f"${money}", True, (255, 255, 255))
        screen.blit(money_text, (10, 10))

        bet_text = font.render(f"bet: ${bet}", True, (255, 255, 255))
        screen.blit(bet_text, (10, 80))

        msg_text = font.render(message, True, (255, 255, 255))
        screen.blit(msg_text, (10, height - 40))

collision_test = CollisionButton(x = 40, y = 260, width = 230, height = 550, color = "red", hover_color = "green", text = None)
collision_test.blit(screen)

bg = pygame.image.load("docs/slots_icons/background.png").convert()
bg = pygame.transform.scale(bg, (width, height))

bg_spin = pygame.image.load("docs/slots_icons/background_2.png").convert()
bg_spin = pygame.transform.scale(bg, (width, height))


def slots_main(collision_test, money):
    running = True
    clock = pygame.time.Clock()

    while running:
        max_bet = money
        
        screen.fill((0, 0, 0))
        
        draw()
        pygame.display.flip()
        time.sleep(0.5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            
                if event.key == pygame.K_UP:
                    if bet < max_bet and bet < money:
                        bet += 1
                
                if event.key == pygame.K_RIGHT:
                    if bet < max_bet and bet < money:
                        bet += 10

                if event.key == pygame.K_LEFT:
                    if bet > min_bet:
                        bet -= 10

                if event.key == pygame.K_DOWN:
                    if bet > min_bet:
                        bet -= 1


                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if collision_test.clicked(pos):
                        bg = bg_spin
                        if money >= bet and bet > 0:
                            money -= bet
                            grid = spin_grid()
                            payout = get_payout(grid, bet)
                            
                            if payout > 0:
                                money += payout
                                message = f"you won ${payout}!"
                            else:
                                message = "you lost!"
                        else:
                            message = "no money left!"

        clock.tick(60)

    pygame.quit()

slots_main(collision_test, money)