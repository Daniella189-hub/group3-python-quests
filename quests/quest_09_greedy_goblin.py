#!/usr/bin/python3
"""Quest 9: The Greedy Goblin - the modulo operator."""
gold = 27
friends = 4
each = gold // friends     # whole pieces per friend
remainder = gold % friends  # what the goblin keeps
print(f"Each friend gets {each} gold; the goblin keeps {remainder}.")
