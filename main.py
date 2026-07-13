from functions import *

def main():
    guessRemaining = 6
    with open('wordList.txt', 'r') as file:
        words = file.read().splitlines()
    while guessRemaining > 0:
        guess = get_guess()
        feedback = get_feedback()
        words = filter_words(words, guess, feedback)
        if len(words) <= 20:
            print("Remaining possible words:", words)
        else:
            print(f"Remaining possible words: {len(words)}")
        guessRemaining -= 1
    print("No more guesses remaining. Game over.")

main()