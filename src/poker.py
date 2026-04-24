import random
from collections import Counter
from itertools import combinations
import os
import time

def clear_screen():
    if os.name == 'nt':
        os.system('CLS')
    else:
        os.system('clear')

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
    straight = ranks == list(range(ranks[0], ranks[0]-5, -1))
    if ranks == [14,5,4,3,2]:
        straight = True
        ranks = [5,4,3,2,1]
    if flush and ranks == [14,13,12,11,10]:
        return (10, ranks)
    if flush and straight:
        return (9, ranks)
    if counts == [4,1]:
        return (8, [count.most_common(1)[0][0]])
    if counts == [3,2]:
        return (7, [count.most_common(1)[0][0]])
    if flush:
        return (6, ranks)
    if straight:
        return (5, ranks)
    if counts == [3,1,1]:
        return (4, [count.most_common(1)[0][0]])
    if counts == [2,2,1]:
        pairs = sorted([r for r,c in count.items() if c==2], reverse=True)
        return (3, pairs)
    if counts == [2,1,1,1]:
        return (2, [count.most_common(1)[0][0]])
    return (1, ranks)

def best_hand(seven):
    best = None
    for five in combinations(seven,5):
        score = evaluate(list(five))
        if best is None or score > best:
            best = score
    return best

def ai_strength(hand, community):
    combined = hand + community
    if len(combined)<5:
        return max(c[0] for c in combined)
    score = best_hand(combined)
    return score[0]

def ai_action(player_idx, hand, community, chips, current_bet, to_call, pot, position):
    strength = ai_strength(hand, community)
    stack = chips[player_idx]
    if strength <= 2:
        fold_prob, call_prob, raise_prob = 0.5,0.4,0.1
    elif strength <= 5:
        fold_prob, call_prob, raise_prob = 0.2,0.6,0.2
    elif strength <= 7:
        fold_prob, call_prob, raise_prob = 0.1,0.5,0.4
    else:
        fold_prob, call_prob, raise_prob = 0.0,0.3,0.7
    if pot > stack*0.3 and strength>2:
        call_prob+=0.1
        fold_prob-=0.1
    call_prob=min(call_prob,1.0)
    fold_prob=max(fold_prob,0.0)
    if position>=2:
        raise_prob+=0.1
        call_prob-=0.05
        fold_prob-=0.05
    total=fold_prob+call_prob+raise_prob
    fold_prob/=total
    call_prob/=total
    raise_prob/=total
    rand=random.random()
    if rand<fold_prob:
        return 'fold',0
    elif rand<fold_prob+call_prob:
        bet=min(to_call,stack)
        return 'call',bet
    else:
        if strength<=4:
            low,high=5,min(15,stack)
        elif strength<=7:
            low,high=10,min(25,stack)
        else:
            low,high=20,min(40,stack)
        if low>high:
            raise_amount=stack
        else:
            raise_amount=random.randint(low,high)
        return 'raise',raise_amount

def betting_round(players, active, chips, pot, community, current_bet=0):
    bets=[0]*len(players)
    ai_moves=[]
    while True:
        changed=False
        if active.count(True)==1:
            return pot
        for i in range(len(players)):
            if not active[i]:
                continue
            to_call=current_bet-bets[i]
            if i==0:
                clear_screen()
                print(f"\nYour turn")
                print(f"Your cards: {' '.join(card_str(c) for c in players[i])}")
                if community:
                    print(f"Community cards: {' '.join(card_str(c) for c in community)}")
                else:
                    print("Community cards: None yet")
                print(f"Pot: {pot} | Your chips: {chips[0]}")
                print(f"Current bet: {current_bet}\nTo call: {to_call}\n")
                if ai_moves:
                    print("AI moves so far this round:")
                    for move in ai_moves:
                        print(move)
                while True:
                    action=input("check, call, raise, fold: ").lower()
                    if action=="fold":
                        active[i]=False
                        remaining=next((j for j,a in enumerate(active) if a),None)
                        if remaining is not None:
                            chips[remaining]+=pot
                            print("You fold")
                            print(f"Player {remaining+1} wins the pot")
                        return pot
                    elif action=="raise":
                        if chips[i]>=to_call+10:
                            chips[i]-=to_call+10
                            bets[i]+=to_call+10
                            pot+=to_call+10
                            current_bet+=10
                            changed=True
                            print(f"You raise to {current_bet}")
                            break
                        else:
                            print("Not enough chips to raise. You must call or fold.")
                            continue
                    elif action=="call" and to_call>0:
                        if chips[i]>=to_call:
                            chips[i]-=to_call
                            bets[i]+=to_call
                            pot+=to_call
                            print("You call")
                            break
                        else:
                            print("Not enough chips to call. You must fold.")
                            continue
                    elif action=="check" and to_call==0:
                        print("You check")
                        break
                    else:
                        print("Invalid action. Try again.")
                        continue
            else:
                position=i
                action,amount=ai_action(i,players[i],community,chips,current_bet,to_call,pot,position)
                if action=='fold':
                    active[i]=False
                    move=f"Player {i+1} folds"
                    ai_moves.append(move)
                elif action=='call':
                    chips[i]-=amount
                    bets[i]+=amount
                    pot+=amount
                    move=f"Player {i+1} calls"
                    ai_moves.append(move)
                elif action=='raise':
                    total_raise=to_call+amount
                    if total_raise>chips[i]:
                        total_raise=chips[i]
                    chips[i]-=total_raise
                    bets[i]+=total_raise
                    pot+=total_raise
                    current_bet=max(current_bet,bets[i])
                    changed=True
                    move=f"Player {i+1} raises to {current_bet}"
                    ai_moves.append(move)
                print(move)
                time.sleep(1)
        if all(not active[i] or bets[i]==current_bet for i in range(len(players))):
            break
    return pot

def play():
    chips=[100]*4
    dealer=0
    while sum(c>0 for c in chips)>1:
        clear_screen()
        print(f"--- New Hand ---")
        deck=new_deck()
        random.shuffle(deck)
        players=[[deck.pop(),deck.pop()] for _ in range(4)]
        active=[chips[i]>0 for i in range(4)]
        pot=0
        community=[]
        starting_bet=5
        for i in range(4):
            if active[i]:
                chips[i]-=starting_bet
                pot+=starting_bet
        print(f"Your hole cards: {' '.join(card_str(c) for c in players[0])}")
        print(f"Automatic starting bet of {starting_bet} chips from each player. Pot is now {pot}.")

        pot=betting_round(players,active,chips,pot,community)
        if sum(active)==1:
            winner=next((i for i,a in enumerate(active) if a),None)
            if winner is not None:
                chips[winner]+=pot
                print(f"Player {winner+1} wins the pot")
            if input("Start a new hand? (y/n): ").lower()!='y':
                break
            continue

        community=[deck.pop() for _ in range(3)]
        print(f"Flop: {' '.join(card_str(c) for c in community)}")
        pot=betting_round(players,active,chips,pot,community)
        if sum(active)==1:
            winner=next((i for i,a in enumerate(active) if a),None)
            if winner is not None:
                chips[winner]+=pot
                print(f"Player {winner+1} wins the pot")
            if input("Start a new hand? (y/n): ").lower()!='y':
                break
            continue

        community.append(deck.pop())
        print(f"Turn: {card_str(community[-1])}")
        pot=betting_round(players,active,chips,pot,community)
        if sum(active)==1:
            winner=next((i for i,a in enumerate(active) if a),None)
            if winner is not None:
                chips[winner]+=pot
                print(f"Player {winner+1} wins the pot")
            if input("Start a new hand? (y/n): ").lower()!='y':
                break
            continue

        community.append(deck.pop())
        print(f"River: {card_str(community[-1])}")
        pot=betting_round(players,active,chips,pot,community)
        if sum(active)==1:
            winner=next((i for i,a in enumerate(active) if a),None)
            if winner is not None:
                chips[winner]+=pot
                print(f"Player {winner+1} wins the pot")
            if input("Start a new hand? (y/n): ").lower()!='y':
                break
            continue

        results={}
        for i in range(4):
            if active[i]:
                results[i]=best_hand(players[i]+community)
        if results:
            winner=max(results,key=lambda k: results[k])
            chips[winner]+=pot
            print(f"Player {winner+1} wins the pot")
        print("Current chip counts:")
        for i,c in enumerate(chips):
            print(f"Player {i+1}: {c}")
        if input("Start a new hand? (y/n): ").lower()!='y':
            break
        dealer=(dealer+1)%4
    winner=max(range(4),key=lambda i: chips[i])
    print(f"Game over! Player {winner+1} wins with {chips[winner]} chips.")

play()