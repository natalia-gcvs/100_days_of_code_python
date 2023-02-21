#Step 5
from replit import clear
from hangman_words import word_list
from hangman_art import logo, stages
import random

print(logo)
chosen_word = random.choice(word_list)

print(chosen_word)

display = []
for blank in chosen_word:
  display += '_'

print(' '.join(display) + '\n')

lives = 6
end_of_game = False


while not end_of_game:
  guess = input('Guess a letter: ')

  clear()

  if guess in display:
    print(f"You've already guessed {guess}.")

  for index, letter in enumerate(chosen_word):
    if letter == guess:
      display[index] = letter

  print(' '.join(display) + '\n')

  if guess not in chosen_word:
    print(f"You've guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print('You lose.')

  if "_" not in display:
    end_of_game = True
    print('You win')

  print(stages[lives])