# Choosing a random number
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to set difficulty

def set_difficulty():
    level = input("Choose the difficulty. Type 'easy' and 'hard'.")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else :
        return HARD_LEVEL_TURNS    


# Check the guess with actual number

def check_answer(guess, answer,turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer :
        print("Too low")
        return turns - 1
    else :
        print(f"You got it right, answer is {answer}")
        return turns


def game():
    """ Function let you the play the number guessing game """
    print("Welcome to the guessing game")
    print("We're guessing from 1 to 100")

    answer = randint(1,100)


    turns = set_difficulty()

    guess = 0
    # Let the user guess the number
    while guess != answer :
        print(f"You've {turns} attempts to make the right guess")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)

        if(turns == 0) : 
            print("You've run out of guess, you lose.")
        elif guess != answer :
            print("Guess Again. ")    

 
game()


