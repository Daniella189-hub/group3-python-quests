#!/usr/bin/python3
# Quest 18: The Loop of Riddles - guessing game
secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    if guess != secret_number:
        print("Wrong! Try again.")
print("Congratulations! You guessed it!")
