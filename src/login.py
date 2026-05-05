#Pseudocode

#import classes
from classes import *

#import helper
from helper import *

import pygame


#login function
def login(screen, users_dict, action):
#parameters: screen, user dictionary, action

    #search dictionary function
    def search(user_dict, searching):
    #parameters: dictionary, searching

        #return true if username exists
        return searching in user_dict

    pygame.init()

    #create messages
    title = Message("This is the login for the DINO CASINO!",300,500)
    username_input = Message("Please input your username here:",300,500)
    password_input = Message("Please input your password here: ",300,400)
    incorrect_pass = Message("Sorry that password is incorrect please enter the correct password.",300,400)
    incorrect_user = Message("Sorry that is an invalid username. Please enter a valid username.",300,400)

    #create input boxes
    input_box_name = TextInput(300, 300, 140, 32)
    input_box_pass = TextInput(300, 100, 140, 32)

    #variables to store input
    username = ""
    password = ""

    running = True

    #while true
    while running:

        #clear screen every frame
        screen.fill((0,0,0))

        #event loop
        for event in pygame.event.get():

            #if quit button clicked
            if event.type == pygame.QUIT:
                running = False
                return "quit"

            #show a welcome message and explain the login
            title.draw(screen)

            #if they choose to create a new user
            if action == "2":

                #ask for username
                username_input.draw(screen)
                username = input_box_name.handle_event(event)

                #ask for password
                password_input.draw(screen)
                password = input_box_pass.handle_event(event)

                #if enter key pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:

                        #create dictionary entry
                        users_dict[username] = {
                            "password": hash_pass(password),
                            "money": 100
                        }

                        #return good
                        return "good"

            #else if they choose login
            elif action == "1":

                #ask for username
                username_input.draw(screen)
                username = input_box_name.handle_event(event)

                #ask for password
                password_input.draw(screen)
                password = input_box_pass.handle_event(event)

                #if enter key pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:

                        #call search
                        output = search(users_dict, username)

                        #if username exists
                        if output == True:

                            #hash entered password
                            hashed_password = hash_pass(password)

                            #get password from dictionary
                            dict_pass = users_dict[username]["password"]

                            #if password matches
                            if hashed_password == dict_pass:

                                #return good
                                return "good"

                            #else show incorrect password
                            else:
                                incorrect_pass.draw(screen)

                        #else show incorrect username
                        else:
                            incorrect_user.draw(screen)

            #else if they choose to exit
            elif action == "3":
                running = False
                #return quit
                return "quit"

        #draw input boxes
        input_box_name.draw(screen)
        input_box_pass.draw(screen)

        #update screen
        pygame.display.flip()


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

        #clear screen
        screen.fill((0,0,0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            #if login was clicked run login and with action being 1
            if login_button.is_clicked(event):
                login(screen, user_dict, "1")

            #else if they choose to sign up run login with action being 2
            if sign_up_button.is_clicked(event):
                login(screen, user_dict, "2")

            #else if they choose to exit run login with action being 3
            if exit_button.is_clicked(event):
                login(screen, user_dict, "3")

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

            


