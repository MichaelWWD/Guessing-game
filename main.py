#Number Guessing Game Objectives:
import random
from art import logo

def hints (choice,answer) :
  if choice == answer :
    print(f"{answer} is correct ,You win  ")
  if choice < answer :
    print("Too low ")
  if choice > answer :
    print("Too High")

print(logo)
print("Welcome to the Guessing Game")
print("I'm thinking of a number between 1 and 100")

number = random.randint(0,100)
print(f"Psst the answer is: ({number})")
guess_limit = 10
difficulty = input("Choose a difficulty type 'easy' or 'hard' : ").lower()
if difficulty == 'easy':
  print(f"You have {guess_limit} attempts")
elif difficulty == 'hard':
  guess_limit = 5
  print(f"You have {guess_limit} attempts")
option = int(input("Make a guess : "))
if option == number :
  print(f"you win ,{number} is correct")
else:
 hints(option,number)
 guess_limit -= 1
 print(f"You have {guess_limit} remaining") 
while guess_limit !=0 and option!= number :
  if option == number :
    print(f"You win, {number} is correct")
  else:
    option = int(input("guess again : "))
    hints(option,number)
    guess_limit -= 1
    print(f"You have {guess_limit} attempts remaining") 

