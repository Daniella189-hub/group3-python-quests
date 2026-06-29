#!/usr/bin/python3
"""Quest 14: The Logical Gatekeeper - and, or, not."""
while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError: print("Invalid input")
while True:
    try:
        gold = int(input("How much gold do you have? "))
        break
    except ValueError: print("Invalid input")
if age >= 18 and gold >= 20:
    print("You may enter the club!")
else:
    print("Sorry, you cannot enter.")
