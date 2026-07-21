def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = "".join(c if c in guesses else "_" for c in secret_word)
        print(display)
        return all(c in guesses for c in secret_word)

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ")
    guess_func = make_hangman(secret_word)

    won = False
    while not won:
        letter = input("Guess a letter: ")
        won = guess_func(letter)

    print("You won! The word was:", secret_word)