alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encode(text, shift):
    text_encoded = ''
    for letter in text:
        if letter not in alphabet:
            letter = letter
            text_encoded += letter
        else:
            letter = alphabet[alphabet.index(letter) + shift]
            text_encoded += letter
    print(text_encoded)


def caesar_cypher():
    should_continue = True

    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift = -26 + shift % 26

        if direction == 'decode':
            shift = -26 - shift % 26

        encode(text, shift)

        play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
        if play_again == 'no':
            should_continue = False


caesar_cypher()
