#import all the things
from blackjack import *
from login import *
from poker import *
from slots import *
from view_profile import *
from work import *
from classes import *

pygame.init()

screen_x = 1320
screen_y = 960
font = pygame.font.SysFont("Arial", 12)
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()

running = True

shop_button = ImageButton()

while running:
    pass

#main function
def main():
#parameters: none
    #while true
    while True:
        #call login function
        dictionary = load_df("docs/users.csv")
        move_on = login_ui(dictionary)
        #if it returns quit
        if move_on == "quit":
            #show a message about leaving
            print("Thanks for using Dino Casino!")
            #break
            break 
        #else:
        else:
            dictionary = move_on
            #while true
            while True:
                #choice is them choosing a button of the action they want to complete
                print("""Welcome to Dino Casino! Please choose an action to complete:
                      1. Shop
                      2. Poker
                      3. Blackjack
                      4. Slots
                      5. Work
                      6. Exit""")
                choice = input("Please input the number of the action you would like to complete: ")
                #if they choose edit profile(shop)
                if choice == "1":
                    display_profile()
                    pass
                #else if they choose poker
                elif choice == "2":
                    poker_main()
                    pass
                #else if they choose blackjack
                elif choice == "3":
                    blackjack_main()
                    pass
                #else if they choose slots
                elif choice == "4":
                    slots_main()
                    pass
                #else if they choose to work
                elif choice == "5":
                    work()
                    pass
                #else if they choose exit
                elif choice == "6":
                    save_df(dictionary, "docs/users.csv")
                    #break
                    break