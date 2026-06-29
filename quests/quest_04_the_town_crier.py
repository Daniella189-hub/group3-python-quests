#!/usr/bin/python3
"""Quest 4: The Town Crier - build a message from validated input."""
city_name = input("Enter a city name: ")

while True:
    try:
        current_year = int(input("Enter the current year: "))
        break
    except ValueError:
        print("That wasn't a valid year. Please enter digits only (e.g. 2026).")

your_name = input("Enter your name: ")
print(f"Welcome to {city_name}! The year is {current_year}, "
      f"and our newest resident is {your_name}.")
