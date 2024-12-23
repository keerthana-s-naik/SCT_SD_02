import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("I have picked a number between 1 and 100. Can you guess it?\n")

    while True:
        try:
            # Prompt the user to input their guess
            user_guess = int(input("Enter your guess : "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again...\n")
            elif user_guess > number_to_guess:
                print("Too high! Try again...\n")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.\n")
                break
        except ValueError:
            print("Please enter a valid number.!\n")

if __name__ == "__main__":
    guess_the_number()
