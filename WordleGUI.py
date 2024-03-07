import nltk
import time
import random
nltk.data.path.append('/work/words')
# nltk.download('words', download_dir='/work/words') # Uncomment this to download. Only needed for the first time you run the code.
from nltk.corpus import words

### TODO Change the dictionary. This one is very weird

word_list = words.words()
words_five = [word.lower() for word in word_list if len(word) == 5]

correct_word = random.choice(words_five)

print(correct_word) # for testing purposes

guess_count = 0
print("Welcome to Wordle! The game where you guess a 5 letter word (no plurals). You have 10 guesses. Good luck!")
while True:
    try:
        if guess_count > 0 and guess_count < 10:
            print(f"You have {10 - guess_count} guesses left.")
        print("Enter your guess: ")
        guess = input()
        guess = guess.lower()
        if guess not in words_five:
            raise ValueError("Sorry, that is not a five letter word. Try again!")
        else:
            guess_count += 1
            print(f"your guess is: \n{guess}")
            for i in range(5):
                if guess[i] == correct_word[i]: # if the letter is in the word AND in the correct position
                    print(guess[i], end="")
                elif guess[i] in correct_word:  # if the letter is in the word but not in the correct position
                    print("+", end="")
                else:   # if the letter is not in the word
                    print("-", end="")
            print()
            if guess == correct_word:
                print(f"Congratulations! You guessed the word in {guess_count} guesses!")
                break
            elif guess_count == 10:
                print(f"Sorry, you ran out of guesses. The word was {correct_word}.")
                break
    except ValueError as err:
        print(err)
