import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while True:
        print("\nWord:", display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1
            print_hangman(incorrect_guesses)

            if incorrect_guesses == max_attempts:
                print("You ran out of attempts!")
                print("The word was:", word)
                break

def print_hangman(incorrect_guesses):
    stages = [
        """
         -----
         |   |
         |
         |
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |   |
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  \|/
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  \|/
         |   |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  \|/
         |   |
         |  /
        ---
        """,
        """
         -----
         |   |
         |   O
         |  \|/
         |   |
         |  / \\
        ---
        """,  
    ]
    print(stages[incorrect_guesses])

hangman()
