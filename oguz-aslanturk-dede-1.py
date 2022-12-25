# Mehmet OGUZ
# Hatice Berna ASLANTURK
# Cagdas DEDE

# HOMEWORK QUESTION 1

# importing the random module
import random


def Run():
    number_to_guess = random.randint(1, 1000)
    print("I have a number between 1 to 1000.")
    print("Can you guess my number?")

    result = False
    guess_count = 1

    while not result:
        result = CheckGuess(number_to_guess)
        guess_count += 1

    PrintResult(guess_count)


def CheckGuess(number_to_guess):
    user_guess = GetUserGuess()

    if number_to_guess == user_guess:
        print("Excellent!! You guessed the number!!!")
        return True
    else:
        if number_to_guess > user_guess:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        return False


def PrintResult(guess_count):
    if guess_count == 10:
        print("Ahah! You know the secret!")
    else:
        if guess_count > 10:
            print("You should be able to do better!!!")
        else:
            print("Either you know the secret or you got lucky")


def GetUserGuess():
    while True:
        try:
            user_guess = int(input("Please type your first guess: "))
        except ValueError:
            print("Please enter a valid integer 1-1000")
            continue
        if 1 <= user_guess <= 1000:
            return user_guess
        else:
            print('The integer must be in the range 1-1000')


Run()

