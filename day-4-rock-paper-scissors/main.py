rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random

user_choice = input('Rock, Paper or Scissors? ').lower()

computer_choice = random.choice(['rock', 'paper', 'scissors'])

if user_choice == 'rock':
    print(rock)
elif user_choice == 'paper':
    print(paper)
elif user_choice == 'scissors':
    print(scissors)

if computer_choice == 'rock':
    print(f'computer chose:\n{rock}')
elif computer_choice == 'paper':
    print(f'computer chose:\n{paper}')
elif computer_choice == 'scissors':
    print(f'computer chose:\n:{scissors}')

if computer_choice == 'rock' and user_choice == 'scissors':
    print('You lose.')
elif computer_choice == 'scissors' and user_choice == 'paper':
    print('You lose.')
elif computer_choice == 'paper' and user_choice == 'rock':
    print('You lose.')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win.')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win.')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win.')
elif computer_choice == user_choice:
    print('Draw')
elif user_choice != 'paper' or user_choice != 'scissor' or user_choice != 'rock':
    print('You lose.')














