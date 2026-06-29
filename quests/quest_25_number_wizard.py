#!/usr/bin/python3
import random

secret_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != secret_number:
    if guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess again: "))

print("That's right! The number was", secret_number)
