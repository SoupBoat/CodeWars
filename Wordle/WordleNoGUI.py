import random

"""
This is an odler version of whats in the WordleGUI. That one has custom games while this does not. 
Its just more robust and customisable outside of code thats all.
"""


# uses the scrabble dictionary to get a list of words
# the list is then filtered to only include words with 5 letters
# for this code to run wordleDictionary.txt must be in the same directory
word_list = []
with open('sowpods.txt', 'r') as f:
    line = f.readline().strip()
    word_list.append(line)
    while line:
        line = f.readline().strip()
        word_list.append(line)
word_list.pop() # remove the last element which is an empty string

words_five = [word.lower() for word in word_list if len(word) == 5]
correct_word = random.choice(words_five)

# print(correct_word) # for testing purposes

guess_count = 0
print("Welcome to Wordle! The game where you guess a 5 letter word (no plurals). You have 10 guesses. Good luck!")
while True:
    try:
        if guess_count > 0 and guess_count < 10:
            print(f"You have {10 - guess_count} guesses left.")
        print("Enter your guess: ")
        word = input()
        word = word.lower()
        if len(word) != 5:
            raise ValueError("Sorry, that is not a five letter word. Try again!")
        if word not in words_five:
            raise ValueError("Sorry, its not a word in my dictionary. Try again!")
        else:
            guess_count += 1
            print(f"your guess is: \n{word}")
            for i in range(5):
                if word[i] == correct_word[i]: # if the letter is in the word AND in the correct position
                    print(word[i], end="")
                elif word[i] in correct_word:  # if the letter is in the word but not in the correct position
                    print("+", end="")
                else:   # if the letter is not in the word
                    print("-", end="")
            print()
            if word == correct_word:
                print(f"Congratulations! You guessed the word in {guess_count} guesses!")
                break
            elif guess_count == 10:
                print(f"Sorry, you ran out of guesses. The word was {correct_word}.")
                break
    except ValueError as err:
        print(err)
