#import all the things
from blackjack import *
from login import *
from poker import *
from slots import *
from view_profile import *
from work import *
from classes import *

pygame.init()

#screen_x = 1320
#screen_y = 960
#font = pygame.font.SysFont("Arial", 12)
#screen = pygame.display.set_mode((screen_x, screen_y))
#clock = pygame.time.Clock()

#running = True

#shop_button = ImageButton()

#while running:
    #pass

#main function
def main():
#parameters: none
    pygame.init()
    screen = pygame.display.set_mode((2000,1100))
    pygame.display.set_caption("User Profile")
    title = Message("Dino Casino",500,50,size=100)
    poker = Button(1000,100,"docs/buttons/small_button.png",scale=0.25,text="Poker")
    profile = Button(1000,200,"docs/buttons/mid_button.png",scale=0.25,text="Profile")
    blackjack = Button(1000,300,"docs/buttons/large_button.png",scale=0.25,text="Blackjack")
    slots = Button(1000,400,"docs/buttons/small_button.png",scale=0.25,text="Slots")
    exit = Button(1000,500,"docs/buttons/small_button.png",scale=0.25,text="Exit")

    running = True

    #while true
    while running:
        #call login function
        dictionary = load_df("docs/CSVs/users.csv")
        move_on = login_ui(dictionary)
        if move_on != "quit":
            user = dictionary[move_on]
        #if it returns quit
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                running = False
            # mouse click
            if exit.is_clicked(event):
                running = False
            if move_on == "quit":
                running = False

            if poker.is_clicked(event):
                dictionary=poker_main(dictionary,move_on)
                save_df(dictionary,"docs/CSVs/users.csv")
            if profile.is_clicked(event):
                display_profile(user)
            if blackjack.is_clicked(event):
                dictionary=blackjack_main(dictionary,move_on)
                save_df(dictionary,"docs/CSVs/users.csv")
            if slots.is_clicked(event):
                money = user["money"]
                slots_main(grid,message,money,bet,bg,dictionary,move_on)

        title.draw(screen)
        poker.draw(screen)
        blackjack.draw(screen)
        slots.draw(screen)
        exit.draw(screen)
        pygame.display.flip()
    pygame.quit
            

                
        

main()