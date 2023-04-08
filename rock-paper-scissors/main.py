rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

rps = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

user_choice = int(input())
if user_choice < 0 or user_choice > 2 :
  print("You enter an invalid number. You lose!")
else :
  print(f"{rps[user_choice]}\n")
  computer_random_choice = random.randint(0,2)
  print("Computer: ")
  print(rps[computer_random_choice])
  
  if user_choice - computer_random_choice == 1 :
    print("You win!")
  elif user_choice - computer_random_choice == 2 :
    print("You lose!")
  elif user_choice - computer_random_choice == -1 :
    print("You lose!")
  elif user_choice - computer_random_choice == -2 :
    print("You win!")
  elif user_choice - computer_random_choice == 0 :
    print("It's a draw. Play again!")
