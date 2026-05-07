# MH 1st view profile functions
import pygame
import sys
from csv_management import *
# display avatar:
def display_avatar(user, window):
    # load avatar base
    avatar = pygame.image.load(user["avatar base"]).convert_alpha()
    # loop over their inventory, if an item is equipped load it
    for item in user["inventory"]:
        if item.value == "equipped":
            equipped_item = pygame.image.load(user["inventory"][item]).convert_alpha()
    window.blit(avatar, (100, 100))
    window.blit(equipped_item, (100, 100))

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
    # runs display avatar
    display_avatar(user)
    # runs display inventory
    display_inventory(user)
    # runs display info
    display_info(user)

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
