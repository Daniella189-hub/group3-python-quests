#!/usr/bin/python3
# This program is a simple guessing game. It keeps asking the user
# to guess the secret number until the correct number is entered.
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Wrong guess. Try again!")
