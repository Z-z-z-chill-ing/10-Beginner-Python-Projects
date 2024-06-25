import random, re

lives = 10
continue_bool = True
wins = 0

def logic(guess, lives, wins):
    if (abs(guess - rand_num) == 0):
        wins += 1
        print(f"Congrets, you guess correct number, it was {rand_num}.")
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

while (lives > 0):
    limit = input("Up to what number guessing number should be: ")
    while (bool(re.search(pattern='[a-zA-Z]', string=limit))):
        print("The value can only be an integer.\n")
        limit = input("Up to what number guessing number should be: ")
    rand_num = random.randint(1, int(limit))
    while (continue_bool and lives):
        guess = int(input("\nGuess the number: "))
        continue_bool, lives, wins = logic(guess, lives, wins)
    if (lives == 0):
        print("Sorry, but it still was a great run.")
    continue_game = input("Do you wish to continue playing?[y/n]: ")
    if (continue_game.lower() == "n"):
        break
    else:
        lives = 10
        continue_bool = True
