import nltk
import random
nltk.data.path.append('/work/words')
# nltk.download('words', download_dir='/work/words') # Uncomment this to download. Only needed for the first time you run the code.
from nltk.corpus import words
import tkinter as tk

### TODO Change the dictionary. This one is very weird
"""
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
        if len(guess) != 5:
            raise ValueError("Sorry, that is not a five letter word. Try again!")
        if guess not in words_five:
            raise ValueError("Sorry, its not a word in my dictionary. Try again!")
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
"""

# this function is used to center the window
def center_window(width, height):
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


class WelcomeWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Wordle - Welcome!")
        center_window(300, 250)
        
        #start game button. sends you to the next page to start guessing
        start_button = tk.Button(self, text="Start Game!", width=10, command = self.on_game_start)
        start_button.pack(padx=20, pady=(20, 10))   # the 20 is above and the 10 is below

        #rules button. sends you to the next page to read the rules
        rules_button = tk.Button(self, text="Rules", width=10, command = self.on_rules)
        rules_button.pack(padx=20, pady=10)

        #quit button. kills the window
        quit_button = tk.Button(self, text="Quit", width=10, command = self.on_quit)
        quit_button.pack(padx=20, pady=(10, 20))

        self.pack()
    
    # go to game page
    def on_game_start(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        GameStart(self.master)

    # go to rules page
    def on_rules(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        RulesWindow(self.master)

    # quit the window
    def on_quit(self):
        self.master.destroy()

class RulesWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Wordle - Rules")
        center_window(300, 250)
        
        #rules for the game
        rules1 = tk.Label(self, text="The rules are simple. You have 10 guesses to guess a 5 letter word. No plurals.", wraplength=200)
        rules1.pack(padx=10, pady=(20, 10))

        #good luck message
        rules2 = tk.Label(self, text="Good luck!")
        rules2.pack(pady=10)
        
        #back button. sends you back to the welcome page so you can start game
        back_button = tk.Button(self, text="Back", width=10, command = self.on_back)
        back_button.pack(pady=(10, 20))

        self.pack()

    # go back to welcome page
    def on_back(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)

class GameStart(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Wordle - Game")
        center_window(300, 250)
        F1 = tk.Frame(self, bg = "blue")
        tk.Label(F1, bg = "blue", text="Enter your guess:", width = 30).grid(row=0, column=0)
        tk.Label(F1, bg = "green", text="You have 10 guesses.").grid(row=0, column=1)
        tk.Label(F1, bg =  "yellow", text="No plurals.").grid(row=0, column=2)
        tk.Label(F1, text="aaaaa").grid(row=0, column=3)
        F1.grid(row=0, column=0)

        
        tk.Label(self, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        submit_button = tk.Button(self, text="Submit", width=8,command = self.on_successful_login)
        submit_button.grid(row=2, column=1, sticky="e", padx=10, pady=(10, 0))

        submit_button = tk.Button(self, text="Back", width=8, command = self.on_back)
        submit_button.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))

        self.pack()
 
    def on_back(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)  

    def on_successful_login(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)   


window = tk.Tk()
window.geometry("600x400")








WelcomeWindow(window)
window.mainloop()