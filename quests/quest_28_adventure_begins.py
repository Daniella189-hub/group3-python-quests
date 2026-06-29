#!/usr/bin/python3

def forest():
    print("You are in a dark forest.")
    choice = input("Go left or right? ")

    if choice == "left":
        print("You found a peaceful village. Good ending!")
    else:
        print("You got lost in the forest. Bad ending!")


def cave():
    print("You enter a mysterious cave.")
    choice = input("Light a torch or go deeper? ")

    if choice == "light":
        print("You discover ancient drawings. Good ending!")
    else:
        print("You fall into a trap. Bad ending!")


print("Welcome to The Adventure Begins!")
path = input("Choose forest or cave: ")

if path == "forest":
    forest()
else:
    cave()
