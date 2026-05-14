import pygame
import random
import sys

pygame.init()

width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blackjack")

font = pygame.font.SysFont("arial", 28)
big_font = pygame.font.SysFont("arial", 42)

green = (20, 120, 20)
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 50, 50)
blue = (50, 100, 200)
gray = (180, 180, 180)
yellow = (255, 215, 0)

clock = pygame.time.Clock()

money = 100
min_bet = 1
bet = 10

def create_deck():
    deck = []

    for _ in range(4):
        deck.extend([
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            "J", "Q", "K", "A"
        ])

    random.shuffle(deck)
    return deck

def deal_hand(deck, amount=2):
    hand = []

    for _ in range(amount):
        hand.append(deck.pop())

    return hand

def calculate_total(hand):
    total = 0
    aces = 0

    for card in hand:

        if card in ["J", "Q", "K"]:
            total += 10

        elif card == "A":
            total += 11
            aces += 1

        else:
            total += card

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

def hit(deck, hand):
    hand.append(deck.pop())

class BetButton:
    def __init__(self, x, y, w, h, text, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, black, self.rect, 3)

        txt = font.render(self.text, True, white)

        screen.blit(
            txt,
            (
                self.rect.x + self.rect.width // 2 - txt.get_width() // 2,
                self.rect.y + self.rect.height // 2 - txt.get_height() // 2,
            ),
        )

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

def draw_card(card, x, y):
    rect = pygame.Rect(x, y, 80, 120)

    pygame.draw.rect(screen, white, rect)
    pygame.draw.rect(screen, black, rect, 3)

    txt = big_font.render(str(card), True, black)

    screen.blit(
        txt,
        (
            x + rect.width // 2 - txt.get_width() // 2,
            y + rect.height // 2 - txt.get_height() // 2,
        ),
    )

def draw_text(text, x, y, color=white, big=False):
    current_font = big_font if big else font
    img = current_font.render(text, True, color)
    screen.blit(img, (x, y))

def start_new_hand(state):

    if len(state["deck"]) < 15:
        state["deck"] = create_deck()

    if state["money"] < state["bet"]:
        state["message"] = "not enough money"
        return

    state["money"] -= state["bet"]

    state["player_hand"] = deal_hand(state["deck"])
    state["dealer_hand"] = deal_hand(state["deck"])

    state["message"] = ""
    state["game_over"] = False

    player_total = calculate_total(state["player_hand"])
    dealer_total = calculate_total(state["dealer_hand"])

    if player_total == 21 and dealer_total == 21:
        state["message"] = "both blackjack"
        state["money"] += state["bet"]
        state["game_over"] = True

    elif player_total == 21:
        state["message"] = "blackjack"
        state["money"] += int(state["bet"] * 2.5)
        state["game_over"] = True

    elif dealer_total == 21:
        state["message"] = "dealer blackjack"
        state["game_over"] = True

def dealer_turn(state):

    while calculate_total(state["dealer_hand"]) < 17:
        hit(state["deck"], state["dealer_hand"])

    player_total = calculate_total(state["player_hand"])
    dealer_total = calculate_total(state["dealer_hand"])

    if dealer_total > 21:
        state["message"] = "dealer busted"
        state["money"] += state["bet"] * 2

    elif player_total > dealer_total:
        state["message"] = "you win"
        state["money"] += state["bet"] * 2

    elif player_total < dealer_total:
        state["message"] = "dealer wins"

    else:
        state["message"] = "push"
        state["money"] += state["bet"]

    state["game_over"] = True

def draw_game(state, buttons):

    screen.fill(green)

    draw_text(f"money: ${state['money']}", 40, 30, yellow, True)
    draw_text(f"bet: ${state['bet']}", 40, 80)

    draw_text("dealer", 100, 100)

    if state["game_over"]:

        for i, card in enumerate(state["dealer_hand"]):
            draw_card(card, 100 + i * 100, 150)

        draw_text(
            f"total: {calculate_total(state['dealer_hand'])}",
            100,
            300
        )

    else:

        draw_card(state["dealer_hand"][0], 100, 150)

        hidden = pygame.Rect(200, 150, 80, 120)
        pygame.draw.rect(screen, red, hidden)
        pygame.draw.rect(screen, black, hidden, 3)

    draw_text("player", 100, 380)

    for i, card in enumerate(state["player_hand"]):
        draw_card(card, 100 + i * 100, 430)

    draw_text(
        f"total: {calculate_total(state['player_hand'])}",
        100,
        580
    )

    draw_text(state["message"], 520, 250, white, True)

    if not state["game_over"]:
        buttons["hit"].draw()
        buttons["stand"].draw()

    buttons["new_hand"].draw()

state = {
    "money": 100,
    "bet": 10,
    "deck": create_deck(),
    "player_hand": [],
    "dealer_hand": [],
    "message": "",
    "game_over": False
}

start_new_hand(state)

buttons = {
    "hit": BetButton(100, 620, 180, 50, "hit", blue),
    "stand": BetButton(320, 620, 180, 50, "stand", red),
    "new_hand": BetButton(700, 620, 220, 50, "new hand", gray)
}

def blackjack_main():

    running = True
    
    while running:

        max_bet = money

        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_UP:
                        if bet < max_bet and bet < money:
                            bet += 1

                    if event.key == pygame.K_RIGHT:
                        if bet + 10 <= money:
                            bet += 10

                    if event.key == pygame.K_LEFT:
                        if bet - 10 >= min_bet:
                            bet -= 10

                    if event.key == pygame.K_DOWN:
                        if bet - 1 >= min_bet:
                            bet -= 1
                            
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                if buttons["hit"].clicked(pos) and not state["game_over"]:

                    hit(state["deck"], state["player_hand"])

                    if calculate_total(state["player_hand"]) > 21:
                        state["message"] = "you busted"
                        state["game_over"] = True

                elif buttons["stand"].clicked(pos) and not state["game_over"]:

                    dealer_turn(state)

                elif buttons["new_hand"].clicked(pos):

                    start_new_hand(state)

        draw_game(state, buttons)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

blackjack_main()