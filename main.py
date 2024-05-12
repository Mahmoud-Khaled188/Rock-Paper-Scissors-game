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


user_choice = int(input("Type 0 for rock, 1 for scissors or 2 for paper.\n"))
import random
pc_choice = random.randint(0,2)
game_images = [rock, scissors, paper]
print(game_images[user_choice])
print("computer chose:")
print(game_images[pc_choice])
if user_choice == 0:
  if pc_choice == 1:
    print("You win!")
  elif pc_choice == 2:
    print("You lose!")
  else:
    print("Draw!")
elif user_choice == 1:
  if pc_choice == 0:
    print("You lose!")
  elif pc_choice == 2:
    print("You win!")
  else:
    print("Draw!")
else:
  if pc_choice == 0:
    print("You win!")
  elif pc_choice == 1:
    print("You lose!")
  else:
    print("draw")
  
  
  
  

