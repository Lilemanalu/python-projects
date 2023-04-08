print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Welcome to Treasure Island
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure and become the richest pirate in the world!\n")

# Crossroad
print("You are at a crossroad. There are two paths ahead. One leads to the treasure and the other leads to certain doom.")
path = input("Which path will you take? Type 'left' or 'right': ").lower()

if path == "left":
  # Lake
  print("\nYou have reached a lake. There is a boat tied to a tree. Type 'wait' to wait for the boat or 'swim' to swim across the lake.")
  lake_choice = input().lower()
  if lake_choice == "wait":
    # Doors
    print("\nYou reach an island with three doors - one red, one blue, and one yellow. Which door do you choose?")
    door_choice = input("Type 'red', 'blue', or 'yellow': ").lower()
    if door_choice == "red":
      print("\nYou opened the door and were burned alive by a dragon. Game over!")
    elif door_choice == "blue":
      print("\nYou opened the door and were mauled by a pack of wild beasts. Game over!")
    elif door_choice == "yellow":
      print("\nYou opened the door and found the treasure! Congratulations, you are the richest pirate in the world!")
    else:
      print("\nYou couldn't make a decision and starved to death on the island. Game over!")
  else:
    print("\nYou were attacked by a giant octopus while swimming. Game over!")
else:
  print("\nYou fell into a deep hole and died. Game over!")
