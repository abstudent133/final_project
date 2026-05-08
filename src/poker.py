import pygame
import random
from collections import Counter
from itertools import combinations
import sys

def poker_main():
    pygame.init()

    width, height = 1200, 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Texas Hold'em Poker")

    font = pygame.font.SysFont("arial", 24)
    big_font = pygame.font.SysFont("arial", 36)

    green = (20, 120, 20)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (200, 50, 50)
    blue = (50, 100, 200)
    gray = (180, 180, 180)
    yellow = (255, 215, 0)

    clock = pygame.time.Clock()

    def new_deck():
        return [(r, s) for r in range(2, 15) for s in "SHDC"]

    def card_str(card):
        faces = {11: "J", 12: "Q", 13: "K", 14: "A"}
        r, s = card
        return f"{faces.get(r, r)}{s}"

    def evaluate(hand):
        ranks = sorted([c[0] for c in hand], reverse=True)
        suits = [c[1] for c in hand]

        count = Counter(ranks)
        counts = sorted(count.values(), reverse=True)

        flush = len(set(suits)) == 1
        straight = ranks == list(range(ranks[0], ranks[0] - 5, -1))

        if ranks == [14, 5, 4, 3, 2]:
            straight = True
            ranks = [5, 4, 3, 2, 1]

        if flush and ranks == [14, 13, 12, 11, 10]:
            return (10, ranks)
        if flush and straight:
            return (9, ranks)
        if counts == [4, 1]:
            return (8, ranks)
        if counts == [3, 2]:
            return (7, ranks)
        if flush:
            return (6, ranks)
        if straight:
            return (5, ranks)
        if counts == [3, 1, 1]:
            return (4, ranks)
        if counts == [2, 2, 1]:
            return (3, ranks)
        if counts == [2, 1, 1, 1]:
            return (2, ranks)

        return (1, ranks)

    def best_hand(seven):
        best = None

        for five in combinations(seven, 5):
            score = evaluate(list(five))

            if best is None or score > best:
                best = score

        return best

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

    chips = [100] * 4
    pot = 0
    message = ""

    deck = new_deck()
    random.shuffle(deck)

    players = [[deck.pop(), deck.pop()] for _ in range(4)]
    community = []

    active = [True] * 4

    check_btn = Button(50, 600, 150, 50, "check", blue)
    call_btn = Button(250, 600, 150, 50, "call", green)
    raise_btn = Button(450, 600, 150, 50, "raise", yellow)
    fold_btn = Button(650, 600, 150, 50, "fold", red)
    next_btn = Button(950, 600, 180, 50, "next round", gray)

    def draw_card(card, x, y):
        rect = pygame.Rect(x, y, 70, 100)

        pygame.draw.rect(screen, white, rect)
        pygame.draw.rect(screen, black, rect, 2)

        txt = font.render(card_str(card), True, black)
        screen.blit(txt, (x + 10, y + 35))

    def draw_text(text, x, y, color=white, big=False):
        current_font = big_font if big else font
        img = current_font.render(text, True, color)
        screen.blit(img, (x, y))

    def draw_table():
        screen.fill(green)

        draw_text(f"Pot: {pot}", 540, 40, yellow, True)

        draw_text("Community Cards", 460, 120)

        for i, card in enumerate(community):
            draw_card(card, 420 + i * 90, 170)

        draw_text("Your Hand", 70, 420)

        for i, card in enumerate(players[0]):
            draw_card(card, 70 + i * 90, 470)

        for i in range(1, 4):
            draw_text(f"AI {i} Chips: {chips[i]}", 850, 100 + i * 80)

        draw_text(f"Your Chips: {chips[0]}", 50, 40)

        draw_text(message, 50, 540)

        check_btn.draw()
        call_btn.draw()
        raise_btn.draw()
        fold_btn.draw()
        next_btn.draw()

    def ai_turn():
        global pot
        global message

        for i in range(1, 4):
            if not active[i]:
                continue

            action = random.choice(["call", "raise", "fold"])

            if action == "fold":
                active[i] = False
                message = f"AI {i} folds"

            elif action == "call":
                bet = 5
                chips[i] -= bet
                pot += bet
                message = f"AI {i} calls"

            elif action == "raise":
                bet = 10
                chips[i] -= bet
                pot += bet
                message = f"AI {i} raises"

    stage = 0

    def next_round(stage, community, deck, pot, message):

        if stage == 0:
            community.extend([deck.pop(), deck.pop(), deck.pop()])
            message = "flop dealt"

        elif stage == 1:
            community.append(deck.pop())
            message = "turn dealt"

        elif stage == 2:
            community.append(deck.pop())
            message = "river dealt"

        elif stage == 3:
            showdown()

        stage += 1

    def showdown():
        global message
        global pot

        results = {}

        for i in range(4):
            if active[i]:
                results[i] = best_hand(players[i] + community)

        winner = max(results, key = lambda x: results[x])

        chips[winner] += pot

        if winner == 0:
            message = "you win the pot"
        else:
            message = f"AI {winner} wins the pot"

        pot = 0

    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if check_btn.clicked(pos):
                    message = "you check"
                    ai_turn()

                elif call_btn.clicked(pos):
                    chips[0] -= 5
                    pot += 5
                    message = "you call"
                    ai_turn()

                elif raise_btn.clicked(pos):
                    chips[0] -= 10
                    pot += 10
                    message = "you raise"
                    ai_turn()

                elif fold_btn.clicked(pos):
                    active[0] = False
                    message = "you folded"

                elif next_btn.clicked(pos):
                    next_round(stage, community, deck, pot, message)

        draw_table()

        pygame.display.flip()

    pygame.quit()
    sys.exit()