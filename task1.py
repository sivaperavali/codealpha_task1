import random

def hangman_game():
    word_list = ['python', 'hangman', 'programming', 'developer', 'algorithm']
    selected_word = random.choice(word_list)
    guessed_word = ['_'] * len(selected_word)
    attempts_left = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"The word has {len(selected_word)} letters.")
    print(" ".join(guessed_word))
    
    while attempts_left > 0 and '_' in guessed_word:
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in selected_word:
            print("Good guess!")
            for i, letter in enumerate(selected_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print("Incorrect guess.")
            attempts_left -= 1
        
        print(f"Word: {' '.join(guessed_word)}")
        print(f"Attempts left: {attempts_left}")

    if '_' not in guessed_word:
        print("Congratulations! You guessed the word:", selected_word)
    else:
        print("Game over! The word was:", selected_word)

# Run the game
hangman_game()