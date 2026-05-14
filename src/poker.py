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
        unique = sorted(set(ranks), reverse=True)

        straight = False

        if len(unique) == 5:
            if unique[0] - unique[-1] == 4:
                straight = True
            if unique == [14, 5, 4, 3, 2]:
                straight = True
                unique = [5, 4, 3, 2, 1]

        if flush and unique == [14, 13, 12, 11, 10]:
            return (10, unique)
        if flush and straight:
            return (9, unique)
        if counts == [4, 1]:
            return (8, ranks)
        if counts == [3, 2]:
            return (7, ranks)
        if flush:
            return (6, ranks)
        if straight:
            return (5, unique)
        if counts == [3, 1, 1]:
            return (4, ranks)
        if counts == [2, 2, 1]:
            return (3, ranks)
        if counts == [2, 1, 1, 1]:
            return (2, ranks)

        return (1, ranks)

    def best_hand(seven):
        best = None
        for c in combinations(seven, 5):
            v = evaluate(list(c))
            if best is None or v > best:
                best = v
        return best

    class Button:
        def __init__(self, x, y, w, h, text, color):
            self.rect = pygame.Rect(x, y, w, h)
            self.text = text
            self.color = color

        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, black, self.rect, 3)
            t = font.render(self.text, True, white)
            screen.blit(t, (self.rect.centerx - t.get_width() // 2,
                            self.rect.centery - t.get_height() // 2))

        def clicked(self, pos):
            return self.rect.collidepoint(pos)

    def reset_round(players):
        deck = new_deck()
        random.shuffle(deck)

        for p in players:
            p["hand"] = [deck.pop(), deck.pop()]
            p["bet"] = 0
            p["folded"] = False
            p["acted"] = False
            p["all_in"] = False

        return deck, players, [], 0, 0, 0

    def next_player(players, i):
        n = len(players)
        for k in range(1, n + 1):
            j = (i + k) % n
            if not players[j]["folded"] and not players[j]["all_in"]:
                return j
        return None

    def alive(players):
        return [i for i, p in enumerate(players) if not p["folded"]]

    def round_done(players, current_bet):
        for p in players:
            if not p["folded"] and not p["all_in"]:
                if not p["acted"]:
                    return False
                if p["bet"] != current_bet:
                    return False
        return True

    def apply_bet(p, amount):
        amount = min(amount, p["chips"])
        p["chips"] -= amount
        p["bet"] += amount
        if p["chips"] == 0:
            p["all_in"] = True
        return amount

    def draw_card(card, x, y):
        r = pygame.Rect(x, y, 70, 100)
        pygame.draw.rect(screen, white, r)
        pygame.draw.rect(screen, black, r, 2)
        t = font.render(card_str(card), True, black)
        screen.blit(t, (x + 10, y + 35))

    def draw_text(text, x, y, color=white, big=False):
        f = big_font if big else font
        screen.blit(f.render(text, True, color), (x, y))

    def draw(players, community, pot, msg):
        screen.fill(green)

        draw_text(f"POT: {pot}", 520, 20, yellow, True)
        draw_text(msg, 40, 520)

        draw_text(f"Player Money: {players[0]['chips']}", 40, 40, white, False)

        draw_text("Community", 480, 100)
        for i, c in enumerate(community):
            draw_card(c, 420 + i * 90, 150)

        draw_text("Player hand", 60, 380)
        for i, c in enumerate(players[0]["hand"]):
            draw_card(c, 60 + i * 90, 430)

        for i in range(1, 4):
            p = players[i]
            status = "folded" if p["folded"] else f"chips {p['chips']} | bet {p['bet']}"
            draw_text(f"AI {i}: {status}", 850, 120 + i * 80)

    def ai(p, current_bet):
        if p["folded"] or p["all_in"]:
            return

        diff = current_bet - p["bet"]

        if diff > 0:
            if random.random() < 0.2:
                p["folded"] = True
                p["acted"] = True
                return
            apply_bet(p, diff)
            p["acted"] = True
            return

        if random.random() < 0.5:
            apply_bet(p, min(10, p["chips"]))
        p["acted"] = True

    deck, players, community, stage, pot, turn = reset_round([
        {"hand": [], "chips": 100, "folded": False, "bet": 0, "acted": False, "all_in": False}
        for _ in range(4)
    ])

    current_bet = 0
    msg = "Game start"

    check = Button(50, 600, 150, 50, "check", blue)
    call = Button(250, 600, 150, 50, "call", green)
    raiseb = Button(450, 600, 150, 50, "raise", yellow)
    fold = Button(650, 600, 150, 50, "fold", red)

    running = True

    while running:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                p = players[0]

                if turn == 0:

                    if check.clicked(pos):
                        if p["bet"] == current_bet:
                            p["acted"] = True
                        msg = "check"

                    elif call.clicked(pos):
                        apply_bet(p, current_bet - p["bet"])
                        p["acted"] = True
                        msg = "call"

                    elif raiseb.clicked(pos):
                        apply_bet(p, min(10 + (current_bet - p["bet"]), p["chips"]))
                        current_bet = max(current_bet, p["bet"])
                        p["acted"] = True
                        msg = "raise"

                    elif fold.clicked(pos):
                        p["folded"] = True
                        p["acted"] = True
                        msg = "fold"

                if players[0]["acted"]:
                    turn = next_player(players, turn)

        alive_players = alive(players)

        if len(alive_players) == 1:
            w = alive_players[0]
            players[w]["chips"] += pot
            msg = f"Player {w} wins (folds)"
            pot = 0
            deck, players, community, stage, pot, turn = reset_round(players)
            current_bet = 0
            continue

        while turn != 0:
            ai(players[turn], current_bet)
            turn = next_player(players, turn)

        if round_done(players, current_bet):
            for p in players:
                pot += p["bet"]
                p["bet"] = 0
                p["acted"] = False

            current_bet = 0

            if stage == 0:
                community.extend([deck.pop(), deck.pop(), deck.pop()])
                msg = "Flop"
            elif stage == 1:
                community.append(deck.pop())
                msg = "Turn"
            elif stage == 2:
                community.append(deck.pop())
                msg = "River"
            elif stage == 3:
                scores = {i: best_hand(players[i]["hand"] + community)
                          for i in range(4) if not players[i]["folded"]}

                if scores:
                    win = max(scores, key=scores.get)
                    players[win]["chips"] += pot
                    msg = f"Player {win} wins"
                else:
                    msg = "All folded"

                pot = 0
                deck, players, community, stage, pot, turn = reset_round(players)
                current_bet = 0
                continue

            stage += 1
            turn = 0

        draw(players, community, pot, msg)

        check.draw()
        call.draw()
        raiseb.draw()
        fold.draw()

        pygame.display.flip()

    money = players[0]["chips"]

    pygame.quit()
    sys.exit()


poker_main()