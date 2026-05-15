# ...existing code...
#import all the things
from blackjack import *
from login import *
from poker import *
from slots import *
from view_profile import *
from classes import *

# ...existing code...
#main function
def main():
#parameters: none
    pygame.init()
    screen = pygame.display.set_mode((2000,1100))
    pygame.display.set_caption("User Profile")
    clock = pygame.time.Clock()
    title = Message("Dino Casino",500,50,size=100)
    poker = Button(500,200,"docs/buttons/small_button.png",scale=0.25,text="Poker")
    profile = Button(500,300,"docs/buttons/mid_button.png",scale=0.25,text="Profile")
    blackjack = Button(500,400,"docs/buttons/large_button.png",scale=0.25,text="Blackjack")
    slots = Button(500,500,"docs/buttons/small_button.png",scale=0.25,text="Slots")
    exit = Button(1000,500,"docs/buttons/small_button.png",scale=0.25,text="Exit")

    running = True
    # call login once before the main loop
    dictionary = load_df("docs/CSVs/users.csv")
    move_on = login_ui(dictionary)

    # if login requested quit, exit cleanly
    if move_on == "quit":
        pygame.quit()
        return

    # if login UI or another module called pygame.quit(), re-init the display
    if not pygame.display.get_init():
        pygame.display.init()
        screen = pygame.display.set_mode((2000,1100))

    user = dictionary[move_on]

    #while true
    while running:

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                running = False
            # mouse click
            if exit.is_clicked(event):
                running = False

            if poker.is_clicked(event):
                dictionary = poker_main(dictionary, move_on)
                save_df(dictionary,"docs/CSVs/users.csv")
            if profile.is_clicked(event):
                display_profile(user)
            if blackjack.is_clicked(event):
                dictionary = blackjack_main(dictionary, move_on)
                save_df(dictionary,"docs/CSVs/users.csv")
            if slots.is_clicked(event):
                # note: grid, message, bet, bg must be defined before calling slots_main
                money = user["money"]
                dictionary = slots_main(grid, message, money, bet, bg, dictionary, move_on)
                save_df(dictionary,"docs/CSVs/users.csv")

        screen.fill((0, 0, 0))

        title.draw(screen)
        poker.draw(screen)
        blackjack.draw(screen)
        slots.draw(screen)
        exit.draw(screen)
        profile.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
# ...existing code...

main()