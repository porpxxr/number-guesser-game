# --- Number Guessing Game ---
# This is the template file for the collaborative Git tutorial.

def get_player_guess():
    def get_player_guess():
    while True:
        try:
            guess = int(input("กรุณาทายตัวเลข (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("โปรดป้อนตัวเลขระหว่าง 1 ถึง 100 เท่านั้น")
        except ValueError:
            print("โปรดป้อนตัวเลขที่ถูกต้อง")

def check_guess(secret_number, player_guess):
    """
    Task for Student 2:
    1. Compare the player's guess with the secret number.
    2. If the guess is correct, return the string "correct".
    3. If the guess is too high, return the string "high".
    4. If the guess is too low, return the string "low".
    """
    if player_guess == secret_number:
        return "correct"
    elif player_guess > secret_number:
        return "high"
    else:  # player_guess < secret_number
        return "low"

def play_game():
    """
    The main function to run the game.
    This part is already complete.
    """
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    import random
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        attempts += 1
        guess = get_player_guess()
        result = check_guess(secret_number, guess)

        if result == "correct":
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif result == "high":
            print("Too high! Try again.")
        elif result == "low":
            print("Too low! Try again.")

if __name__ == "__main__":
    play_game()
