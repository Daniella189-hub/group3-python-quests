#!/usr/bin/python3
# This program asks the user for their name and quest,
# then displays a personalized greeting using a function
# with parameters.
def personalized_greeting(name, quest):
    print(f"Welcome, {name}!")
    print(f"Good luck on your quest: {quest}!")

name = input("Enter your name: ")
quest = input("Enter your quest: ")

personalized_greeting(name, quest)
