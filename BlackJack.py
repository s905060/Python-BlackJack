#!/usr/bin/env python
"""
BlackJack Game
@Created by s905060 in 2013.
Inspired by Ene Uran
Python 2.7

"""

from random import choice

"""If Ace or One"""
def game(hand):
    aces = hand.count(11)
    scores = sum(hand)
    if scores > 21 and aces > 0:
        while aces > 0 and scores > 21:
            scores -= 10
            aces -= 1
    return scores

"""Card decks"""
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
aiwon = 0  
pwon = 0

"""Games"""
while True:
    player = []
    player.append(choice(cards))
    player.append(choice(cards))
    pboom = False  
    aiboom = False 
    player_scores = 0
    AI_scores = 0

    """Player_Move""" 
    while True:
        player_scores = game(player)
        print ("You have these cards %s with a total value of %d" % (player, player_scores))
        if player_scores > 21:
            print ("You are busted!")
            pboom = True
            break

        elif player_scores == 21:
            print ("\a BLACKJACK!!!")
            break

        else:
            hit = raw_input("Hit or Stand (h or s): ").lower()
            if 'h' in hit:
                player.append(choice(cards))
            else:
                break

    """AI_Move"""              
    while True:
        AI = []
        AI.append(choice(cards))
        AI.append(choice(cards))

        while True:
            AI_scores = game(AI)                
            if AI_scores < 18:
                AI.append(choice(cards))
            else:
                break

        print ("the AI has %s for a total of %d" % (AI, AI_scores))

        if AI_scores > 21:
            print ("AI is busted!")
            aiboom = True
            if pboom == False:
                print ("You won!")
                pwon += 1

        elif AI_scores > player_scores:
            print ("AI won!")
            aiwon += 1

        elif AI_scores == player_scores:
            print ("It's a draw!")

        elif player_scores > AI_scores:
            if pboom == False:
                print ("You won!")
                pwon += 1

            elif aiboom == False:
                print ("AI won!")
                aiwon += 1
        break
    print "\n"

    print ("Wins, player = %d  AI = %d" % (pwon, aiwon))
    exit = raw_input("Press Enter to continue (q to quit): ").lower()

    if 'q' in exit:
        break

    print "\n"