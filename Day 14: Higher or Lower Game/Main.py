#Importing of everything
import os
import random
import time

from Art import vs
from Art import logo
from Game_data import Data

print(logo)

Current_Score=0
def game():
  Correct_Answer=True
  global Current_Score
  while Correct_Answer:
    print(f"Current Score is:{Current_Score}")
    # The two choices that exist 
    Choice_A=random.choice(Data)
    print(f"Compare A: {Choice_A['name']}, a {Choice_A['description']}, from {Choice_A['country']}\n")
    Number_A=int(Choice_A['follower_count'])
    
    
    
    print(f"{vs} \n")
    
    Choice_B=random.choice(Data)
    print(f"Compare B: {Choice_B['name']}, a {Choice_B['description']}, from {Choice_B['country']} ")
    Number_B=int(Choice_B['follower_count'])
    
    
    # Compare the two numbers and (loop if correct or Exit the while loop)
    User_Choice= input("Who has more followers? Type 'A' or 'B':")
    User_Choice=User_Choice.lower()
    if (User_Choice=='a' and Number_A>Number_B ) or (User_Choice=='b' and Number_A<Number_B):
      Current_Score+= 1
      print(" Well done! You've got the correct answer.")
      time.sleep(2)
      os.system('clear')
      
      
  
    else:
      os.system('clear')
      Correct_Answer=False
      return Current_Score
      

print(f'''
      Sorry, thats wrong!
      Your total score is: {game()}''')

  
