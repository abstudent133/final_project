# MH 1st view profile functions
import pygame

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
    window = pygame.display.set_mode((800, 600))
    count = 0
    x = 100
    y = 100
    # displays all items in their inventory as buttons
    for item in user["inventory"]:
            item_button = pygame.image.load(user["inventory"][item]).convert_alpha()
            window.blit(item_button, (x, y))

        # if the user selects an unequipped item, ask them if they want to equip it
        # if they do, put it on their avatar sprite and unequip any item already there

# display info:
    # displays user name
    # displays users money

# display profile:
    # runs display avatar
    # runs display inventory
    # runs display info