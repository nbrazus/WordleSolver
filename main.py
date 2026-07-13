from functions import *

def main():
    guessRemaining = 6
    while guessRemaining > 0:
        guess = get_guess()
        feedback = get_feedback()
        remaining = filter_words(guess, feedback)
        if len(remaining) <= 15:
            print("Remaining possible words:", remaining)
        else:
            print(f"Remaining possible words: {len(remaining)}")
        guessRemaining -= 1
    print("No more guesses remaining. Game over.")

main()