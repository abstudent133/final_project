# MH 1st view profile functions
import pygame
import sys
from classes import *
from csv_management import *
# display avatar:


def overlay_images(screen, base_image, top_image, base_x, base_y, top_x, top_y):

    # get rectangles
    base_rect = base_image.get_rect()
    base_rect.topleft = (base_x, base_y)

    # draw avatar/base image
    screen.blit(base_image, base_rect)

    # only draw top image if it exists
    if top_image != None:

        top_rect = top_image.get_rect()
        top_rect.topleft = (top_x, top_y)

        screen.blit(top_image, top_rect)

# display inventory:
def display_inventory():
    hats_raw = load_df("docs/CSVs/hats.csv")
    hats =[]
    x_y = [[50,50],[50,100],[50,150],[50,200],[50,250],[150,50],[150,100],[150,150],[150,200],[150,250],[250,50],[250,100],[250,150],[250,200],[250,250]]
    num = 0
    for hat in hats_raw.keys():
        button = (ImageButton(x_y[num][0],x_y[num][1],hats_raw[hat],scale=0.25),hat)
        hats.append(button)
        num += 1
    return hats



def display_profile(user):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("User Profile")
    clock = pygame.time.Clock()
    avatar = pygame.image.load("docs/characters/trex.png").convert_alpha()
    # hats csv/dictionary
    hats = display_inventory()
    # currently equipped hat
    equipped_item = None
    hat_paths = load_df("docs/CSVs/hats.csv")
    # find equipped item
    for item in user["inventory"].keys():
        if user["inventory"][item] == "equipped":
            equipped_item = pygame.image.load(hat_paths[item]).convert_alpha()

    title = Message("User Profile",500,50,size=50)
    username = Message(f"Name: {user['username']}",400,170)
    money = Message(f"Money: ${user['money']}",400,230)
    change_hat_button = Button(400,320, "docs/buttons/small_button.png", scale=0.25, text="Hats")

    # popup/menu variable
    show_hat_menu = False
    running = True

    while running:

        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                running = False
            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # toggle hat menu
                if change_hat_button.is_clicked(event):
                    show_hat_menu = not show_hat_menu
                # click hat buttons
                if show_hat_menu:
                    for button in hats:
                        buton, name = button
                        if buton.is_clicked(event):
                            # load selected hat
                            equipped_item = pygame.image.load(hat_paths[name]).convert_alpha()
                            # unequip old hat
                            for item in user["inventory"]:
                                if user["inventory"][item] == "equipped":
                                    user["inventory"][item] = "not equipped"
                            # equip new hat
                            user["inventory"][name] = "equipped"
                            # close popup
                            show_hat_menu = False

        title.draw(screen)
        username.draw(screen)
        money.draw(screen)
        change_hat_button.draw(screen)
        overlay_images(screen,avatar,equipped_item,80, 150,100, 100)

        if show_hat_menu:
            pygame.draw.rect(
                screen,
                (60, 60, 60),(850, 130, 300, 450))
            for button in hats:
                buton, name = button
                buton.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
            
user = {"username": "username",
        "avatar base": "docs/characters/trex.png",
        "money": 100,
        "inventory": {"conductor": "equipped"}}
display_profile(user)