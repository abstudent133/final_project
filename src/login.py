#Pseudocode
#import classes
from classes import *
#import helper
from helper import*

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
    
    #while true
    while True:
        #show a welcome message and explain the login
        print("This is the login for the DINO CASINO!")
        #ask if they want create a new user or login or exit
        #escape = false
        escape = False
        #if they choose to create a new user
        if action == "2":
            #ask for a username
            name = input("Please input your desired username here(note: it cannot be forgot because then your account won't work): ")
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
        elif action == "3":
            #return quit
            return "quit"
        #if escape is true:
        if escape == True:
            #continue
            continue

#login interface
def login_ui(user_dict):
#parameters: none
    #set up space
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True
    login_button = Button("Login",200,200,100,50,(250,0,0),(0,0,255))
    sign_up_button = Button("Sign Up",400,200,100,50,(250,0,0),(0,0,255))
    exit_button = Button("Exit",600,200,100,50,(250,0,0),(0,0,255))

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


            


