#Pseudocode
#import classes
from classes import *
#import helper
from helper import *

import pygame

#login function
def login(users_dict):
#parameters: user dictionary
    #search dictionary function
    def search(user_dict, searching):
    #parameters: dictionary, searching
        #for key in dictionary
        for key in user_dict.keys():
            #if seaching == key:
            if searching == key:
                #return true
                return True
            #else:
            else:
                #continue
                continue
        #return false
        return False
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True
    #while true
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #show a welcome message and explain the login
        print("This is the login for the DINO CASINO!")
        #ask if they want create a new user or login or exit
        choice = input("Would you like to |1. Login|2. Create an Account|3. Exit| Input your choice here: ")
        #escape = false
        escape = False
        #if they choose to create a new user
        if choice == "2":
            #ask for a username
            name = input("Please input your desired username here(note: it cannot be forgot because then your account won't work): ")
            #create a user with the user class
            user = User(name)
            #get the formated info and save it to the dictionary
            users_dict[name] = user
            #return good
            return "good"
        #else if they choose login
        elif choice == "1":
            #while true:
            while True:
                #show a message that if they forgot their username they can input forgot
                print("If you forgot your username then input,'forgot' instead to exit and start over.")
                #ask for username
                username = input("Please input your username here:")
                #if username is "forgot"
                if username == "forgot":
                    #escape = true
                    escape = True
                    #break
                    break
                #call search 
                output = search(users_dict, username)
                #if it returns true
                if output == True:
                    #ask for their password
                    while True:
                        password = input("Please input your password here: ")
                        hashed_password = hash_pass(password)
                        dict_pass = users_dict[username]["password"]
                        #if the passsword matches the one in the dictionary
                        if hashed_password == dict_pass:
                            #break
                            break
                        else:
                            print("Sorry that password is incorrect please enter the correct password.")
                    break
                #else:
                else:
                    #show sorry that username doesn't exist please input a valid username
                    print("Sorry that is an invalid username. Please enter a valid username.")
            #return good
            return "good"

        #else if they choose to exit
        elif choice == "3":
            #return quit
            return "quit"
        #if escape is true:
        if escape == True:
            #continue
            continue
        


