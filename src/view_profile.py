# MH 1st view profile functions
import pygame
import sys
from classes import *
from csv_management import *
# display avatar:


def overlay_images(screen, base_image, top_image, base_x, base_y,top_x, top_y):
    #Get rectangles for positioning
    base_rect = base_image.get_rect()
    top_rect = top_image.get_rect()
    
    #Position the base image on the screen
    base_rect.topleft = (base_x, base_y)
    
    #Center the top image rectangle over the base image rectangle
    top_rect.topleft = (top_x, top_y)
    
    #Draw both layers onto the display surface
    screen.blit(base_image, base_rect)
    screen.blit(top_image, top_rect)

# display inventory:
def display_inventory(user):
    hats = user["Inventory"]
    x = 100
    y = 100
    count = 1
    window = pygame.display.set_mode((800, 600))
    # displays all hats as buttons
    # if a hat is not owned by the user put the lock sprite over it
    # if they select a hat they own equip it
    # if they select a hat they don't own ask them if they want to purchase it
    # if they do run the purchase function

# display info:
def display_info(user):
    pass
    # displays user name
    # displays users money

# display profile:
def display_profile(user):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    avatar = pygame.image.load("docs/characters/trex.png").convert_alpha() 
    equipped_item = None
    hats = load_df("docs\CSVs\hats.csv")
    for item in user["inventory"].keys():
        if user['inventory'][item] == "equipped":
            equipped_item = pygame.image.load(hats[item]).convert_alpha()
    user_name = Message(user["username"],200,150)
    money = Message(user["money"],300,150)
    title = Message("User Profile",500,50,size=50)
    running = True
    while running:
        screen.fill((0,0,0))
        #if quit button clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        title.draw(screen)
        user_name.draw(screen)
        money.draw(screen)
        overlay_images(screen,avatar,equipped_item,50,150,60,200)
        pygame.display.flip()
    pygame.quit
        
            

            
    # runs display avatar
    # runs display inventory
    # runs display info

# load buttons
def load_hats():
    hats = {}
    # creates a button for every hat
    conductor = hats["conductor"]["file path"]
    top = hats["top"]["file path"]
    propeller = hats["propeller"]["file path"]
    baseball = hats["baseball"]["file path"]
    sombrero = hats["sombrero"]["file path"]
    burger = hats["burger"]["file path"]
    wizard = hats["wizard"]["file path"]
    crown = hats["crown"]["file path"]
    jester = hats["jester"]["file path"]
    cowboy = hats["cowboy"]["file path"]
    clown = hats["clown"]["file path"]
    dunce = hats["dunce"]["file path"]
    unicorn = hats["unicorn"]["file path"]
    hotdog = hats["hotdog"]["file path"]
    detective = hats["detective"]["file path"]

# purchase, takes in the user dictionary:
    # asks the user if they want to purchase the item
    # if they do save it to their inventory and subtract it's price from their money total, then return the updated dictionary
    # if they don't go back to the main shop
user = {"username": "username",
        "avatar base": "docs/characters/trex.png",
        "money": 100,
        "inventory": {"conductor": "equipped"}}
display_profile(user)