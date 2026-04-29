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
def display(user):
    hats = user["Inventory"]
    x = 100
    y = 100
    count = 1
    window = pygame.display.set_mode((800, 600))
    # displays all hats as buttons
    # if a hat is not owned by the user put the lock sprite over it
    # if they select a hat they own equip it
    # if they select a hat they don't own ask them if they want to go to the shop
    # if they do run the shop function

# display info:
def display_info(user):
    pass
    # displays user name
    # displays users money

# display profile:
    # runs display avatar
    # runs display inventory
    # runs display info