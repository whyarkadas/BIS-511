# Mehmet OGUZ
# Hatice Berna ASLANTURK
# Cagdas DEDE

# HOMEWORK QUESTION 1

# importing the random module
import random


def run():
    try_again = True
    exit_app = False

    while try_again:
        number_to_guess = random.randint(1, 1000)

        if check_first_guess(number_to_guess):
            try_again = check_reply_again()
            exit_app = not try_again
        else:
            try_again = False

    if exit_app:
        return

    result = False
    guess_count = 1
    number_to_guess = random.randint(1, 1000)

    while not result:
        result = check_guess(number_to_guess, False)
        guess_count += 1

    print_result(guess_count)


def check_first_guess(number_to_guess):
    print("I have a number between 1 to 1000.")
    print("Can you guess my number?")

    user_guess = get_user_guess(True)

    if user_guess == number_to_guess:
        print("Excellent!! You guessed the number!!!")
        return True

    return False


def check_reply_again():
    reply = get_play_again()

    if reply == 'y' or reply == 'Y':
        return True
    else:
        return False


def get_play_again():
    while True:
        try:
            reply = input("Would you like to play again (y or n)?")
        except ValueError:
            print("Please enter a valid reply 'y' or 'n'")
            continue
        if reply == 'y' or reply == 'Y' or reply == 'n' or reply == 'N':
            return reply
        else:
            print("Please enter a valid reply 'y' or 'n'")


def check_guess(number_to_guess, is_first_guess):
    user_guess = get_user_guess(is_first_guess)

    if number_to_guess == user_guess:
        print("Excellent!! You guessed the number!!!")
        return True
    else:
        if number_to_guess > user_guess:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        return False


def print_result(guess_count, ):
    if guess_count == 10:
        print("Ahah! You know the secret!")
    else:
        if guess_count > 10:
            print("You should be able to do better!!!")
        else:
            print("Either you know the secret or you got lucky")


def get_user_guess(is_first_guess):
    first_guess_text = ""

    while True:
        try:
            if is_first_guess: first_guess_text = "first "
            user_guess = int(input(f"Please type your {first_guess_text}guess: "))
        except ValueError:
            print("Please enter a valid integer 1-1000")
            continue
        if 1 <= user_guess <= 1000:
            return user_guess
        else:
            print('The integer must be in the range 1-1000')


run()
