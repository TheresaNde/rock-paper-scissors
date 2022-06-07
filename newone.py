import random

#while :

#get user input
def user_fxn():
  user_action = input("Enter a choice ( R for rock, P for paper, S for scissors): ")
  available_options = [ "R", "P", "S" ]
  computer_options = random.choice(available_options)
  print(f"\n Player({user_action}): Computer ({computer_options})\n")
  
    

  if user_action  == computer_options:
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "y":
      return user_fxn()
    print("." + f"Both players selected {user_action}. It's a tie!" )
   #user_fxn()
   #print(f"Both players selected {)user_action}. It's a tie!")
  elif user_action == "R":
      if computer_options == "S":
        print("Rock smashes scissors! You win!")
      else:
        print("Paper covers rock! You lose.")
  elif user_action == "P":
      if computer_options == "R":
        print("Paper covers rock! You win!")
      else:
        print("Scissors cuts paper! You lose.")
  elif user_action == "S":
      if computer_options == "P":
        print("Scissors cuts paper! You win!")
      else:
        print("Rock smashes scissors! You lose.")

  else:
        print("Select valid variable.")



user_fxn()
    
      

    

     # play_again = input("Play again? (y/n): ")
    #if 
       # break