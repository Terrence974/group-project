import math
import random


def guessing_game():
    # Ask the user for the lower and upper bounds of the range
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            if lower_bound < upper_bound:
                break
            else:
                print("The lower bound must be less than the upper bound. Please try again.")
        except ValueError:
            print("Invalid input. Please enter integer values.")

    # Calculate the total number of guesses needed
    total_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))
    print(f"You have {total_guesses} chances to guess the integer!")

    # Generate a random number within the specified range
    secret_number = random.randint(lower_bound, upper_bound)

    # Initialize the counter for the number of guesses made
    guess_count = 0

    # Game loop
    while guess_count < total_guesses:
        guess_count += 1
        while True:
            try:
                user_guess = int(input(f"Guess a number ({lower_bound}, {upper_bound}): "))
                if lower_bound <= user_guess <= upper_bound:
                    break
                else:
                    print(f"Please guess a number within the range ({lower_bound}, {upper_bound}).")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You found the number in {guess_count} tries.")
            return

        # Provide feedback based on the guess
        elif user_guess < secret_number:
            print("You guessed too small!")
            lower_bound = user_guess + 1  # Update the lower bound for the next guess
        else:
            print("You guessed too high!")
            upper_bound = user_guess - 1  # Update the upper bound for the next guess

        print(f"You have {total_guesses - guess_count} guesses left.")

    # If the loop ends, the user didn't find the number within the allowed guesses
    print(f"\nThe number was {secret_number}. Better luck next time!\n")


# Run the game
guessing_game()