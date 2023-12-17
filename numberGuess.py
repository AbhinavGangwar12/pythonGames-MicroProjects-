import random
import os
from numberArt import logo

EASY_DIFFICULTY_TURNS = 10
HARD_DIFFICULTY_TURNS = 5

def setDifficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard : ").lower()
    if level == "hard":
        return HARD_DIFFICULTY_TURNS
    elif level == "easy":
        return EASY_DIFFICULTY_TURNS

def check_ans(guess,number,turns):
    if guess == number:
        print(f"You got it right. The answer was {guess}")
        return
    elif guess < number:
        print("Too low.")
        return turns - 1
    else:
        print("Too high")
        return turns - 1

def game():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    the_number = random.randint(1,100)
    attempts = setDifficulty()
    guess = -1
    while guess != the_number:
        print(f"You have {attempts} attempts left")
        guess = int(input("Make a guess : "))
        attempts = check_ans(guess,the_number,attempts)
        if attempts <= 0:
            print("You ran out of attempts. You lose")
            return
        else:
            print("Guess again")

game()
play = True
while play:
    again = input("Want to play again ?\nEnter 'yes' to play and 'no' to exit : ").lower()
    if again == "yes":
        os.system('cls')
        game()
    else:
        print("Exiting game...")
