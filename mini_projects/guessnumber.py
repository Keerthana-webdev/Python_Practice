import random

def clue1(guess, secret_number):
      if secret_number > 50:
            print("[CLUE] : The number isgreater than 50")
      elif secret_number < 50:
            print("[CLUE] ; The number is lesser than 50")
      elif secret_number == 50:
            print("[CLUE] : Caught in middle")
      else :
            pass
      
def clue2(guess, secret_number):
      if guess > secret_number:
            print(f"[CLUE] ; The number is smaller than {guess}")
      elif guess < secret_number:
            print(f"[CLUE] : The number is greater than {guess}")
      else :
            pass

def clue3(guess, secret_number):
      if secret_number % 3 == 0 and secret_number % 5 == 0:
            print("[CLUE] : The number is divisible by 3 and 5")
      elif secret_number % 3 == 0:
            print("[CLUE] ; The number is divisible by 3")
      elif secret_number % 5 == 0:
            print("[CLUE] : The number is divisible by 5")
      else :
            pass

print("This is a number guessing game coded by Keerthana")
secret_number = random.randint(1, 100)

name = input("What is your sweet name?  ").capitalize()

print(f"Hi {name}, the computer has selected a random number.Can you crack the secret number")
score = int(100)
guess = int(input("Guess the number ( 1 to 100 )>>  "))

if guess == secret_number:
      print("WOW! You guessed it right! You are amazing !")
      win = True
else:
      print("I have a clue for you.Try again")
      clue1(guess, secret_number)
      score -= 10
      guess = int(input("Guess the number ( 1 to 100 )>>  "))
      if guess == secret_number:
            print("WOW !You guessed it right.Try getting it without a clue :) ")
            win = True
      else:
            print("I have a second clue for you.Try again")
            clue2(guess, secret_number)
            score -= 20
            guess = int(input("Guess the number ( 1 to 100 )>>  "))
            if guess == secret_number:
                  print("WOW! You guessed it right.Try getting it without a clue :) ")
                  win = True
            else:
                  print("I have a third clue for you.Try again")
                  clue3(guess, secret_number)
                  score -= 30
                  guess = int(input("Guess the number ( 1 to 100 )>>  "))
                  if guess == secret_number:
                        print("WOW ! You guessed it right.Try getting it without a clue :) ")
                        win = True
                  else:
                        print("You lost.Better luck next time!")
                        win = False

score_required = input("Wanna know your score?  [y/n]  ")
if  score_required == "y" :
      if win == True :
            print(f"You scored {score}")
      else :
            print("You have lost this game.Better luck next time.Your scored an egg :( ")
else:
      pass

print("Thank you for using Keerthana Softwares")      
