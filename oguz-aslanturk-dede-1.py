# Mehmet OGUZ
# Hatice Berna ASLANTURK
# Cagdas DEDE

# HOMEWORK QUESTION 1

# importing the random module
import random


def run():
    number_to_guess = random.randint(1, 1000)
    print("I have a number between 1 to 1000.")
    print("Can you guess my number?")

    result = False
    guess_count = 1

    is_first_guess = True
    while not result:
        result = check_guess(number_to_guess, is_first_guess)
        is_first_guess = False
        guess_count += 1

    print_result(guess_count)


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


def print_result(guess_count):
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
