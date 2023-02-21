from art import logo
import os


def clear():
    return os.system('cls')


print(logo)


def highest_bid(auction):
    highest_bid = 0
    winner = ''
    for key in auction:
        if auction[key] > highest_bid:
            highest_bid = auction[key]
            winner = key
    print(winner)


stop = False
auction = {}

while not stop:
    name = input("What's your name? ")
    bid = float(input("What's your bid? "))

    auction[name] = bid

    more_bidders = input('Are there other users? Type y or n. ')

    if more_bidders == 'y':
        clear()
    else:
        stop = True
        highest_bid(auction)

