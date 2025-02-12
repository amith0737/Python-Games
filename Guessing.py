import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Rules: Guess the number (between 1 and 10). You have 5 attempts.")
    
    # Generate a random number between 1 and 10
    target_number = random.randint(1, 10)
    attempts = 5

    for attempt in range(1, attempts + 1):
        try:
            # Take user input
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            
            # Check the guess
            if guess == target_number:
                print(f"🎉 Congratulations! You guessed the correct number {target_number} in {attempt} attempts.")
                break
            elif guess < target_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
    else:
        # If the loop completes without breaking
        print(f"Sorry, you've used all your attempts. The correct number was {target_number}. Better luck next time!")

# Run the game
number_guessing_game()
