# https://replit.com/@kreier/RockPaperScisssor?v=1 

import random

win   = False
tries = 1

while True:
  while not win:
    user_choices = input("Type (1) for Rock (2) for Paper (3) for Scissors: ")
    try:
      user_choice = int(user_choices)
    except:
      print("Please enter 1 2 or 3")
      continue
  
    ai_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    if user_choice == 1:
      user_choice = 'Rock'
      print(f"You chose {user_choice}. The computer chose {ai_choice}.")
      win = (ai_choice == 'Scissors')
    elif user_choice == 2:
      user_choice = 'Paper'
      print(f"You chose {user_choice}. The computer chose {ai_choice}.")
      win = (ai_choice == 'Rock')
    elif user_choice == 3:
      user_choice = 'Scissors'
      print(f"You chose {user_choice}. The computer chose {ai_choice}.")
      win = (ai_choice == 'Paper')
    else:
      print("Please enter 1 2 or 3")
          
    # checks if user input is the same as computer choice
    if user_choice == ai_choice:
      print("Tie. Play again.\n")
    elif win:
      print('You won!')
      if tries == 1:
        print("You won on your first try!")
      else:
        print(f"It took you {tries} tries to beat a computer!")
      play = input("\nDo you want to play again (Y/N)? ")
      play = play.lower()
      print(' ')
      if play == 'y':
        win   = False
        tries = 0
      else:
        print("Thank you for playing!")
        break      
    else:
      print('You lost.\n')
    tries += 1
  
