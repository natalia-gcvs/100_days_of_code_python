from replit import clear
from art import logo, vs
from game_data import data
import random

score = 0


def guess(count_a, count_b):
    guess = input('Who has more followers? Type "A" or "B": ')
    if guess == 'A':
        return count_a
    else:
        return count_b


def compare_followers(followers_a, followers_b):
    if followers_a > followers_b:
        return followers_a
    else:
        return followers_b


data = data


def play_game():
    print(logo)
    score = 0
    end_of_game = False

    # pick a random item from the list and print it
    item_a = random.choice(data)
    item_b = random.choice(data)
    while item_a == item_b:
        item_b = random.choice(data)

    print(f"Compare A: {item_a['name']}, {item_a['description']}, {item_a['country']}")

    print(vs)

    print(f"Compare B: {item_b['name']},{item_b['description']}, {item_b['country']}")

    user_guess = guess(item_a['follower_count'],
                       item_b['follower_count'])
    answer = compare_followers(item_a['follower_count'], item_b['follower_count'])

    if user_guess != answer:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        end_of_game = True
    else:
        while not end_of_game:
            clear()
            print(logo)

            if user_guess != answer:
                print(f"Sorry, that's wrong. Final score: {score}")
                return

            score += 1
            print(f"You're right! Current score: {score}")

            item_a = item_b
            item_b = random.choice(data)

            print(f"Compare A: {item_a['name']}, {item_a['description']}, {item_a['country']}")

            print(vs)

            print(f"Compare B: {item_b['name']}, {item_b['description']}, {item_b['country']}")

            user_guess = guess(item_a['follower_count'], item_b['follower_count'])
            answer = compare_followers(item_a['follower_count'], item_b['follower_count'])


def is_correct(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == 'a'
    else:
        return guess == 'b'


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, {description}, from {country}"


def play():
    # Add art.
    print(logo)
    end_of_game = False
    score = 0
    account_a = random.choice(data)
    account_b = random.choice(data)

    # Make game repeatable.
    while not end_of_game:

        # Generate a random account from the game data.
        # Make B become the next A.
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input('Who has more followers? Type "A" or "B": ').lower()

        followers_a = account_a['follower_count']
        followers_b = account_b['follower_count']
        iscorrect = is_correct(guess, followers_a, followers_b)

        clear()
        print(logo)

        if iscorrect:
            # Feedback.
            # Score Keeping.
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            end_of_game = True
            print(f"Sorry, that's wrong. Final score: {score}.")


play()


