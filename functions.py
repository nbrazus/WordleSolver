from collections import Counter

def is_valid_word(word, guess, feedback):
    validLetters = []
    invalidLetters = []
    for x, y, z in zip(word, guess, feedback):
        if x != y and z == 'G':
            return False
        if x == y and (z == 'B' or z == 'Y'):
            return False
        if z == "Y" or z == "G":
            validLetters.append(y)
        if z == "B":
            invalidLetters.append(y)
    wordcounter = Counter(word)
    validcounter = Counter(validLetters)
    if not validcounter <= wordcounter:
        return False
    for letter in invalidLetters:
        if wordcounter[letter] != validcounter[letter]:
            return False
    return True

def filter_words(words, guess, feedback):
    return [w for w in words if is_valid_word(w, guess, feedback)]

def get_guess():
    while True:
        guess = input("Enter your guess: ").strip().lower()
        if len(guess) != 5:
            print("Guess must be exactly 5 letters.")
        elif not (guess.isascii() and guess.isalpha()):
            print("Guess must contain only letters A-Z.")
        else:
            return guess
        

def get_feedback():
    while True:
        feedback = input("Enter feedback (G for green, Y for yellow, B for black): ").strip().upper()
        if len(feedback) != 5:
            print("Feedback must be exactly 5 characters.")
        elif not all(c in 'GYB' for c in feedback):
            print("Feedback must only contain G, Y, or B.")
        else:
            return feedback