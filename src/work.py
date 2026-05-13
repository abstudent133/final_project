# MH 1st work function

import random
from csv_management import *

def work(money, user_dict, username):
    customer_dict = load_df("docs/CSVs/customers.csv")
    customer_list = ["Susan McCombs", "Joshua Jermithan", "Freddie Skips", "Tania the Destroyer","Mr. Egg Senior", "Riswalda Hicks", "Ol' Moldy Bones", "That one guy who always buys choclate bars and them throws them at birds.", "Dave Smith", "Anthony Wobble-Legs", "Nancy No-Brains", "Sir Onion-Eyes", "Lord Spiff of West Chedda Town", "Easton Gifford", "Princess Tumbleweed", "Feezlegorp of X2N30-*9"]
    i = 1
    for i in range(3):
        i = 1
    # random customer appears from the customer dictionary and asks their question
        customer = customer_list[random.randint(0, 15)]
        customer = customer_dict[customer]
        print(f"{customer["name"]}: {customer["question"]}")
        # response option are given to the user
        for response in customer["responses"]:
            print(f"{i}. {response}")
            i += 1
        while True:
            choice = input("How do you respond: ")
            if int(choice) > len(customer["responses"]):
                continue
            else:
                choice = customer["responses"][int(choice) - 1]
                print(choice)
                break
        # if the users response is the correct answer add + 10 to earnings
        if choice == customer["correct"]:
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