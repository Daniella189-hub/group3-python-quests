#!/usr/bin/python3

choice = input("Do you go left or right? ")

if choice == "left":
    action = input("Do you swim or wait? ")
    
    if action == "swim":
        print("You swim and find a hidden treasure!")
    else:
        print("You wait and a boat rescues you. Safe ending!")
else:
    print("You chose right and fell into a trap. Game over!")
