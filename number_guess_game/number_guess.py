import random

lives = 10
continueBool = True
wins = 0

def logic(guess, lives, wins, rand_num):
    if (abs(guess - rand_num) == 0):
        wins += 1
        print(f"Congrets, you've guessed a correct number, it was {rand_num}.")
        print(f"Your total count of wins: {wins}.\n")
        return False, lives, wins
    elif (abs(guess - rand_num) > 5 and abs(guess - rand_num) <= 10):
        lives -= 1
        print("Your guess is close.")
        print(f"{lives} lives remaining.\n")
        return True, lives, wins
    elif (abs(guess - rand_num) > 0 and abs(guess - rand_num) <= 5):
        lives -= 1
        print("Your guess is really close.")
        print(f"{lives} lives remaining.\n")
        return True, lives, wins
    elif (abs(guess - rand_num) > 10 and abs(guess - rand_num) <= 20):
        lives -= 1
        print("Your guess, well not that far off.")
        print(f"{lives} lives remaining.\n")
        return True, lives, wins
    else:
        lives -= 1
        print("Your guess is wrong.")
        print(f"{lives} lives remaining.\n")
        return True, lives, wins
    
def start_game(lives, continueBool, wins):
    limit = input("Enter the limit of the guessing number: ")
    while (not limit.strip().isnumeric()):
        print("Limit value shouldn't be empty, and should contain numerical value.")
        limit = input("Enter the limit of the guessing number: ")
    randInt = random.randint(1, int(limit))
    while (lives and continueBool):
        guessNumber = input("Enter your guess: ")
        while (not guessNumber.strip().isnumeric()):
            print("Guess value shouldn't be empty, and should contain numerical value.")
            guessNumber = input("Enter your guess: ")
        continueBool, lives, wins = logic(guess=int(guessNumber), lives=lives, wins=wins, rand_num=randInt)
    continueChoice = input("Do you wish to continue?[y/n]: ")
    if (continueChoice.lower() == "n"):
        return
    else:
        continueBool = True
        lives = 10
        start_game(lives, continueBool, wins)

if __name__ == "__main__":
    start_game(lives, continueBool, wins)