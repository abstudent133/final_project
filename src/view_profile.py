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

def change_character(user):
    pygame.init()
    title = Message("Choose New Character",500,50,size=100)



def display_profile(user):
    pygame.init()
    screen = pygame.display.set_mode((2000,1100))
    pygame.display.set_caption("User Profile")
    clock = pygame.time.Clock()
    avatar = pygame.image.load("docs/characters/trex.png").convert_alpha()
    # hats csv/dictionary
    # currently equipped hat
    equipped_item = None

    title = Message("User Profile",500,50,size=100)
    username = Message(f"Name: {user['username']}",1000,170)
    money = Message(f"Money: ${user['money']}",1000,230)
    exit = Button(1800,1000,"docs/buttons/small_button.png",scale=0.25,text="Exit")
    change_character = Button(1800,900,"docs/buttons/small_button.png",scale=0.25,text="Change Character")
    
    # popup/menu variable
    running = True

    while running:

        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                running = False
            # mouse click
            if exit.is_clicked(event):
                running = False
                

        title.draw(screen)
        username.draw(screen)
        money.draw(screen)
        exit.draw(screen)
        screen.blit(avatar,(0,0))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
            
user = {"username": "username",
        "avatar base": "docs/characters/trex.png",
        "money": 100,
        "inventory": {"conductor hat": "equipped"}}
display_profile(user)