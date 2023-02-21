from art import logo
import random

HARD_LEVEL_NUMBER = 5
EASY_LEVEL_NUMBER = 10
turn = 0


def difficulty():
    level = input('Choose a difficulty. Type "easy" or "hard": ')
    if level == 'easy':
        return EASY_LEVEL_NUMBER
    elif level == 'hard':
        return HARD_LEVEL_NUMBER


def check_answer(guess, number_chosen, turn):
    if guess < number_chosen:
        print('Too low.')
        return turn - 1
    if guess > number_chosen:
        print('Too high.')
        return turn - 1
    if guess == number_chosen:
        print(f'You got it the answer is {number_chosen}')


def game():
    print(logo)

    print("Welcome to the Number Guessing Game.\nI'm thinking of number between 1 and 100.")

    # generate a random number to be guessed
    number_chosen = random.randint(1, 100)
    turn = difficulty()
    guess = 0

    while guess != number_chosen:
        print(f"You have {turn} remaining to guess the number.")
        guess = int(input('Make a guess: '))
        turn = check_answer(guess, number_chosen, turn)

        if turn == 0:
            print("You've run out of guesses. You lose")
            return
        elif guess != number_chosen:
            print('Guess again.')


game()






















