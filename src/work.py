# MH 1st work function

import random
import pygame
from csv_management import *
from classes import *
import time

pygame.init()

def work(money, user_dict, username):
    width, height = 1020, 1020
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Work")
    bg_image = pygame.image.load("file_path").convert()
    bg_image = pygame.transform.scale(bg_image, (1020, 1020))
    customer_dict = load_df("docs/CSVs/customers.csv")
    customer_list = ["Susan McCombs", "Joshua Jermithan", "Freddie Skips", "Tania the Destroyer","Mr. Egg Senior", "Riswalda Hicks", "Ol' Moldy Bones", "That one guy who always buys choclate bars and them throws them at birds.", "Dave Smith", "Anthony Wobble-Legs", "Nancy No-Brains", "Sir Onion-Eyes", "Lord Spiff of West Chedda Town", "Easton Gifford", "Princess Tumbleweed", "Feezlegorp of X2N30-*9"]
    while running:
        for i in range(3):
        # random customer appears from the customer dictionary and asks their question
            customer = customer_list[random.randint(0, 15)]
            customer = customer_dict[customer]
            counter = pygame.image.load("file_path").convert_alpha()
            counter = pygame.transform.scale(sprite, (width, height))
            sprite = pygame.image.load(customer["file_path"]).convert_alpha()
            sprite = pygame.transform.scale(sprite, (width/2, height/2))
            question = Message(f"{customer["name"]}: {customer["question"]}", 0, 300)
            question.draw(screen)
            # response option are given to the user
            response_1 = Button(250, 300, "docs/buttons/large_button.png", 1, customer["responses"][0])
            response_1.draw(screen)
            response_2 = Button(350, 300, "docs/buttons/large_button.png", 1, customer["responses"][1])
            response_2.draw(screen)
            response_3 = Button(450, 300, "docs/buttons/large_button.png", 1, customer["responses"][2])
            response_3.draw(screen)
            response_4 = Button(550, 300, "docs/buttons/large_button.png", 1, customer["responses"][3])
            response_4.draw(screen)
            screen.fill((0,0,0))
            screen.blit(bg_image, (0, 0))
            screen.blit(sprite, (0, 0))
            screen.blit(counter, (0, -375))
            for event in pygame.event.get:
                if event.type == pygame.QUIT:
                    running = False
                # if the user selects the response 1 button check if it is the correct or incorrect response
                if response_1.is_clicked(event):
                    choice = customer["responses"][0]
                    response_1.set_alpha(0)
                    response_2.set_alpha(0)
                    response_3.set_alpha(0)
                    response_4.set_alpha(0)
                    question.set_alpha(0)
                # if the user selects the response 2 button check if it is the correct or incorrect response
                if response_2.is_clicked(event):
                    choice = customer["responses"][1]
                    response_1.set_alpha(0)
                    response_2.set_alpha(0)
                    response_3.set_alpha(0)
                    response_4.set_alpha(0)
                    question.set_alpha(0)
                # if the user selects the response 3 button check if it is the correct or incorrect response
                if response_3.is_clicked(event):
                    choice = customer["responses"][2]
                    response_1.set_alpha(0)
                    response_2.set_alpha(0)
                    response_3.set_alpha(0)
                    response_4.set_alpha(0)
                    question.set_alpha(0)
                # if the user selects the response 4 button check if it is the correct or incorrect response
                if response_4.is_clicked(event):
                    choice = customer["responses"][3]
                    response_1.set_alpha(0)
                    response_2.set_alpha(0)
                    response_3.set_alpha(0)
                    response_4.set_alpha(0)
                    question.set_alpha(0)
            # if the users response is the correct answer add + 10 to earnings
            if choice == customer["correct"]:
                money += 10
                amount = Message("They put ten dollars in your tip jar.", 0, 200)
                response = Message(f"{customer["name"]}: {customer["happy_response"]}", 0, 300)
                amount.draw(screen)
                response.draw(screen)
                time.
                sprite.set_alpha(0)
                response.set_alpha(0)
                amount.set_alpha(0)
            # if the users response is the wrong answer then subtract - 10 from earnings
            elif choice in customer["incorrect"]:
                money -= 10
                response = Message(f"{customer["name"]}: {customer["response"]}", 0, 300)
                response.draw(screen)
                sprite.set_alpha(0)
                response.set_alpha(0)
            # if the users response is a neutral answer add + 5 to earnings
            else:
                money += 5
    user_dict[username]["money"] += money
    # returns the days earnings
    return user_dict
