#Pseudocode
#import classes
from classes import *
#import helper
from helper import *

import pygame

#login function
def login(users_dict, action):
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
    pygame.init
    title = Message("This is the login for the DINO CASINO!",300,500)
    username_input = Message("Please input your username here:",300,500)
    password_input = Message("Please input your password here: ",300,400)
    incorrect_pass = Message("Sorry that password is incorrect please enter the correct password.",300,400)
    incorrect_user = Message("Sorry that is an invalid username. Please enter a valid username.",300,400)
    input_box_name = TextInput(300, 300, 140, 32)
    input_box_pass = TextInput(300, 100, 140, 32)
    running = True
    #while true
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #show a welcome message and explain the login
        title.draw(screen)
        #ask if they want create a new user or login or exit
        #if they choose to create a new user
        if action == "2":
            #ask for a username
            username_input.draw(screen)
            name = input_box_name.handle_event(event)
            #create a user with the user class
            user = User(name)
            #get the formated info and save it to the dictionary
            users_dict[name] = user
            #return good
            return "good"
        #else if they choose login
        elif action == "1":
            #while true:
            while True:
                username_input.draw(screen)
                username = input_box_name.handle_event(event)
                #call search 
                output = search(users_dict, username)
                #if it returns true
                if output == True:
                    #ask for their password
                    while True:
                        password_input.draw(screen)
                        password = input_box_pass.handle_event()
                        hashed_password = hash_pass(password)
                        dict_pass = users_dict[username]["password"]
                        #if the passsword matches the one in the dictionary
                        if hashed_password == dict_pass:
                            #break
                            break
                        else:
                            incorrect_pass.draw(screen)
                    break
                #else:
                else:
                    #show sorry that username doesn't exist please input a valid username
                    incorrect_user.draw(screen)
            #return good
            return "good"

        #else if they choose to exit
        elif action == "3":
            #return quit
            return "quit"
        

#login interface
def login_ui(user_dict):
#parameters: none
    #set up space
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True
    login_button = Button(200,200,100,50,(250,0,0),(0,0,255),"Login")
    sign_up_button = Button(400,200,100,50,(250,0,0),(0,0,255),"Sign Up")
    exit_button = Button(600,200,100,50,(250,0,0),(0,0,255),"Exit")

    #start loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #if login was clicked run login and with action being 1
            if login_button.is_clicked(event):
                login(user_dict, "1")
            #else if they choose to sign up run login with action being 2
            if sign_up_button.is_clicked(event):
                login(user_dict, "2")
            #else if they choose to exit run login with action being 3
            if exit_button.is_clicked(event):
                login(user_dict, "3")

        #draw all of the buttons
        login_button.draw(screen)
        sign_up_button.draw(screen)
        exit_button.draw(screen)
        #show it on the screen
        pygame.display.flip()
    
    pygame.quit()
# DICTIONARY STRUCTURE:
    # users = {
    # username = {
        # password = password
        # money = money
        # avatar_base = avatar_base
        # inventory = {item : equipped, item_2 : unequipped}
    #}
#}    

user_dict = {"Ronald":{"password":"password",
                       "money":100}}

login_ui(user_dict)

            


