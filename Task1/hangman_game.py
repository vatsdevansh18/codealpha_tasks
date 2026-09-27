"""A polished, console-based Hangman game."""

import random


WORDS = [
    ("Programming", "python"),
    ("Programming", "function"),
    ("Technology", "keyboard"),
    ("Space", "planet"),
    ("Music", "guitar"),
]
HANGMAN_STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def display_word(word, guessed_letters):
    """Return the current word progress with unguessed letters hidden."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def get_valid_guess(guessed_letters, hint_available):
    """Request one new letter, or a single optional hint."""
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if guess == "hint":
            if hint_available:
                return guess
            print("You have already used your hint in this game.")
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only, or type 'hint'.")
        elif guess in guessed_letters:
            print(f"You already tried '{guess}'. Choose a different letter.")
        else:
            return guess


def choose_word(word_queue):
    """Return a shuffled word without repeating one in the current round."""
    if not word_queue:
        word_queue.extend(WORDS)
        random.shuffle(word_queue)
    return word_queue.pop()


def play_game(word_queue):
    """Play one complete game and return True when the player wins."""
    category, word = choose_word(word_queue)
    guessed_letters = set()
    incorrect_letters = []
    hint_available = True
    max_mistakes = len(HANGMAN_STAGES) - 1

    print("\n" + "=" * 42)
    print("              HANGMAN")
    print("=" * 42)
    print(f"Category: {category} | You have {max_mistakes} lives and one hint.")

    while len(incorrect_letters) < max_mistakes:
        progress = display_word(word, guessed_letters)
        print(HANGMAN_STAGES[len(incorrect_letters)])
        print(f"\nWord: {progress}")
        print("Incorrect guesses:", ", ".join(incorrect_letters) or "None")
        print(f"Lives remaining: {max_mistakes - len(incorrect_letters)}")

        if "_" not in progress:
            print(f"\nYou won! The word was '{word}'.")
            return True

        guess = get_valid_guess(guessed_letters, hint_available)
        if guess == "hint":
            hidden_letters = [letter for letter in word if letter not in guessed_letters]
            revealed_letter = random.choice(hidden_letters)
            guessed_letters.add(revealed_letter)
            hint_available = False
            print(f"Hint used: the word contains '{revealed_letter}'.")
            continue
        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            incorrect_letters.append(guess)
            print("Not in the word.")

    print(HANGMAN_STAGES[-1])
    print(f"\nOut of lives! The word was '{word}'.")
    return False


def main():
    """Run games until the player chooses to stop."""
    games_played = 0
    wins = 0
    word_queue = []
    while True:
        games_played += 1
        wins += play_game(word_queue)
        print(f"Score: {wins} win(s) from {games_played} game(s).")
        if input("Play again? (y/n): ").lower().strip() not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
