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

def create_deck():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
    random.shuffle(deck)
    return deck

def convert_card(card):
    if card == 11:
        return "J"

    if card == 12:
        return "Q"

    if card == 13:
        return "K"

    if card == 14:
        return "A"

    return card

def deal_hand(deck, amount=2):
    hand = []

    for _ in range(amount):
        hand.append(convert_card(deck.pop()))

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
    hand.append(convert_card(deck.pop()))

class Button:
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

def reset_game(state):
    state["deck"] = create_deck()
    state["player_hand"] = deal_hand(state["deck"])
    state["dealer_hand"] = deal_hand(state["deck"])
    state["message"] = ""
    state["game_over"] = False

def dealer_turn(state):
    while calculate_total(state["dealer_hand"]) < 17:
        hit(state["deck"], state["dealer_hand"])

    player_total = calculate_total(state["player_hand"])
    dealer_total = calculate_total(state["dealer_hand"])

    if dealer_total > 21:
        state["message"] = "dealer busted, you win"
        state["money"] += state["bet"]

    elif player_total > dealer_total:
        state["message"] = "you win"
        state["money"] += state["bet"]

    elif player_total < dealer_total:
        state["message"] = "dealer wins"
        state["money"] -= state["bet"]

    else:
        state["message"] = "tie"

    state["game_over"] = True

def draw_game(state, buttons):
    screen.fill(green)

    draw_text(f"money: ${state['money']}", 40, 30, yellow, True)

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

    draw_text("player", 100, 380)

    for i, card in enumerate(state["player_hand"]):
        draw_card(card, 100 + i * 100, 430)

    draw_text(
        f"total: {calculate_total(state['player_hand'])}",
        100,
        560
    )

    draw_text(state["message"], 560, 220, white, True)

    if not state["game_over"]:
        buttons["hit"].draw()
        buttons["stand"].draw()

    buttons["restart"].draw()

state = {
    "money": 100,
    "bet": 10,
    "deck": create_deck(),
    "player_hand": [],
    "dealer_hand": [],
    "message": "",
    "game_over": False
}

state["player_hand"] = deal_hand(state["deck"])
state["dealer_hand"] = deal_hand(state["deck"])

buttons = {
    "hit": Button(100, 580, 180, 60, "hit", blue),
    "stand": Button(330, 580, 180, 60, "stand", red),
    "restart": Button(700, 580, 200, 60, "new hand", gray)
}

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if buttons["hit"].clicked(pos) and not state["game_over"]:
                hit(state["deck"], state["player_hand"])

                if calculate_total(state["player_hand"]) > 21:
                    state["message"] = "you busted"
                    state["money"] -= state["bet"]
                    state["game_over"] = True

            elif buttons["stand"].clicked(pos) and not state["game_over"]:
                dealer_turn(state)

            elif buttons["restart"].clicked(pos):
                reset_game(state)

    draw_game(state, buttons)

    pygame.display.flip()

pygame.quit()
sys.exit()