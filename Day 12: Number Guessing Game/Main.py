import random
import time
import os
from Art import art

replay_game=True
while replay_game:
  #Inital Opening stuff: 
  print(art)
  print(''' 
    Welcome to the number Guessing Game!
    I'm thinking of a number between 1 and 100. 
  ''')
  number_list=[]
  for i in range(0,101): 
    number_list.append(i)
  Com_num=random.choice(number_list)
  print(f"Psst, the correct answer is: {Com_num} ")
  
  
  #Beginning of the game
  time.sleep(2)
  
  
  Difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")
  
  lives=[5, 10]
  if Difficulty=="easy":
    Lives=lives[1]
  else:
    Lives=lives[0]
  print(f"You have {Lives} attempts to guess the correct number.")
  
  #Process to the game
  Start_game=True
  
  def Number_game():
    global Lives
    global Start_game
    guess=int(input("Make a guess:"))
    if Lives>0:
      if guess>Com_num:
          print("  Too high. Guess again.")
          Lives=Lives-1
          print(f"  You have {Lives} attempts remaining to guess the number.")
      elif guess<Com_num:
        print("  Too Low. Guess again.")
        Lives=Lives-1
        print(f"  You have {Lives} attempts remaining to guess the number.")
      elif guess==Com_num:
        print("Well done! You've won the game!")
        Start_game=False
    if Lives==0 :
      print("Uh oh! You've lost the game!")
      Start_game=False
  
  # Check condtion to make sure 
  
  while Start_game:
    Number_game()


  #Replay the entire game
  restart=input("Would you like to start the game again? Yes or no?")
  if restart=='yes':
    os.system('clear') 
  else:
    print("Thanks for playing the game!")
    replay_game=False
