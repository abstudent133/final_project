# MH 1st work function

import random
import pygame
from csv_management import *
from classes import *

pygame.init()

def work(money, user_dict, username):
    width, height = 1280, 1020
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Work")
    customer_dict = load_df("docs/CSVs/customers.csv")
    customer_list = ["Susan McCombs", "Joshua Jermithan", "Freddie Skips", "Tania the Destroyer","Mr. Egg Senior", "Riswalda Hicks", "Ol' Moldy Bones", "That one guy who always buys choclate bars and them throws them at birds.", "Dave Smith", "Anthony Wobble-Legs", "Nancy No-Brains", "Sir Onion-Eyes", "Lord Spiff of West Chedda Town", "Easton Gifford", "Princess Tumbleweed", "Feezlegorp of X2N30-*9"]
    for i in range(3):
        x = 200, 400
        y = 200, 400

    # random customer appears from the customer dictionary and asks their question
        customer = customer_list[random.randint(0, 15)]
        customer = customer_dict[customer]
        sprite = pygame.image.load(customer["file_path"]).convert()
        sprite = pygame.transform.scale(sprite, (width, height))
        question = Message(customer["question"], x, y)
        question.draw(screen)
        # response option are given to the user
        response_1 = Button(250, 300, "button_path", 1, customer["responses"][0])
        response_2 = Button(250, 300, "button_path", 1, customer["responses"][1])
        response_3 = Button(250, 300, "button_path", 1, customer["responses"][2])
        response_4 = Button(250, 300, "button_path", 1, customer["responses"][3])
        while running:
            screen.fill((0,0,0))
            for event in pygame.event.get:

                if event.type == pygame.QUIT:
                    running = False
                # if the user selects the response 1 button check if it is the correct or incorrect response
                if response_1.is_clicked(event):
                    choice = customer["responses"][0]
                response_1.draw(screen)
                # if the user selects the response 2 button check if it is the correct or incorrect response
                if response_2.is_clicked(event):
                    choice = customer["responses"][1]
                response_2.draw(screen)
                # if the user selects the response 3 button check if it is the correct or incorrect response
                if response_3.is_clicked(event):
                    choice = customer["responses"][2]
                response_3.draw(screen)
                # if the user selects the response 4 button check if it is the correct or incorrect response
                if response_4.is_clicked(event):
                    choice = customer["responses"][3]
                response_4.draw(screen)
        # if the users response is the correct answer add + 10 to earnings
        if choice == customer["correct"]:
            print(customer["happy_response"])
            money += 10
        # if the users response is the wrong answer then subtract - 10 from earnings
        elif choice in customer["incorrect"]:
            money -= 10
            print(f"{customer["name"]}: {customer["response"]}")
        # if the users response is a neutral answer add + 5 to earnings
        else:
            money += 5
    user_dict[username]["money"] += money
    # returns the days earnings
    return user_dict
