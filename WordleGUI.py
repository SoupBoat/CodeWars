import random
import tkinter as tk

#Defaults. On the Custom Page the user can change these values
noLetters = 5  # number of letters in the word. Change this to allow for different length words.
maxGuesses = 6  # number of guesses allowed. Change this to allow for more guesses.

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

        #custom button. sends you to the custom settings page
        custom_button = tk.Button(self, text="Custom", width=10, command = self.on_custom)
        custom_button.pack(padx=20, pady=10)

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

    # go to custom settings page
    def on_custom(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        CustomWindow(self.master)

    # quit the window
    def on_quit(self):
        self.master.destroy()

class RulesWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Wordle - Rules")
        center_window(300, 350)

        ### wordle rules
        # Each guess must be a valid five-letter word.
        #The color of a tile will change to show you how close your guess was.
        #If the tile turns green, the letter is in the word, and it is in the correct spot.
        #If the tile turns yellow, the letter is in the word, but it is not in the correct spot.
        #If the tile turns gray, the letter is not in the word.

        #rules for the game
        rules1 = tk.Label(self, text=f"Each guess must be a valid word.", wraplength=200)
        rules1.pack(padx=10, pady=(20, 10))

        rules2 = tk.Label(self, text=f"The color of a tile will change to show you how close your guess was.", wraplength=200)
        rules2.pack(padx=10, pady=10)

        rules3 = tk.Label(self, bg = "light green", text=f"If the tile turns green, the letter is in the word, and it is in the correct spot.", wraplength=200)
        rules3.pack(padx=10, pady=10)

        rules4 = tk.Label(self, bg = "yellow", text=f"If the tile turns yellow, the letter is in the word, but it is not in the correct spot.", wraplength=200)
        rules4.pack(padx=10, pady=10)

        rules5 = tk.Label(self, bg = "light grey", text=f"If the tile turns gray, the letter is not in the word.", wraplength=200)
        rules5.pack(padx=10, pady=10)
        
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

class CustomWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Wordle - Custom")
        # self.master.resizable(False, False)
        center_window(250, 150)
        
        tk.Label(self, text="Number of Letters:").grid(row=0, column=0)
        self.noLetters_entry = tk.Entry(self)
        self.noLetters_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self, text="Number of Guesses:").grid(row=1, column=0)
        self.maxGuesses_entry = tk.Entry(self)
        self.maxGuesses_entry.grid(row=1, column=1, padx=10, pady=10)
        
        submit_button = tk.Button(self, text="Submit", width=8,command = self.on_submit)
        submit_button.grid(row=2, column=1, sticky="e", padx=10, pady=(10, 0))

        back_button = tk.Button(self, text="Back", width=8, command = self.on_back)
        back_button.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))
        self.pack()
 
    def on_back(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)

    def on_submit(self):
        global noLetters, maxGuesses
        noLetters = int(self.noLetters_entry.get())
        maxGuesses = int(self.maxGuesses_entry.get())

        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)   

class GameStart(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Wordle - Game")
        center_window(300, 400)
        self.guess_count = 0 
        prevGuesses = []

        # uses the scrabble dictionary to get a list of words
        # the list is then filtered to only include words with 5 letters
        # for this code to run wordleDictionary.txt must be in the same directory
        word_list = []
        with open('wordleDictionary.txt', 'r') as f:
            line = f.readline().strip()
            word_list.append(line)
            while line:
                line = f.readline().strip()
                word_list.append(line)
        word_list.pop() # remove the last element which is an empty string

        words_dictionary = [word.lower() for word in word_list if len(word) == noLetters]
        correct_word = random.choice(words_dictionary)
        # print(correct_word) # for testing purposes

        # function to check the word
        # this is where the wordle happens
        def checkWord(event, self=self):    # dont change (event, self=self) it doesn't work otherwise
            word = entryAttempt.get()   # get the word from the entry box
            entryAttempt.delete(0, 'end')   #clear the entry box
            word = word.lower()     # convert the word to lowercase
            
            try:
                # check if the word has already been guessed
                if word in prevGuesses:
                    raise ValueError("You already guessed that word. Try again!")
                # check if the word is 5 letters
                if len(word) != noLetters:
                    raise ValueError(f"Sorry, that is not a {noLetters} letter word. Try again!")
                # check if the word is in the dictionary
                if word not in words_dictionary:
                    raise ValueError("Sorry, its not a word in my dictionary. Try again!")
                
                ####if no errors, then the guess is valid. continue
                prevGuesses.append(word)
                # correctArr is an array of the correct word. it is used for making sure that double letters
                #are correctly processed. eg. if there is only 1 'e' in the word, and the guess has 2 'e's
                #then the first 'e' will be marked as correct and the second 'e' will be marked as incorrect
                correctArr = []
                for i in range(len(correct_word)): correctArr.append(correct_word[i])
                # positionArr is an array of the positions of the green or yellow boxes. it is used for the grey boxes
                positionArr = []
                
                for i in range(noLetters):
                    if word[i] == correct_word[i]: # if the letter is in the word AND in the correct position
                        guessArray[self.guess_count][i].config(text = word[i], bg="light green")
                        # "remove" the letter from correctArr so that it is not counted again
                        correctArr[i] = "0" 
                        positionArr.append(i)
                for i in range(noLetters):
                    if i not in positionArr:
                        if word[i] in correctArr:  # if the letter is in the word but not in the correct position
                            guessArray[self.guess_count][i].config(text = word[i], bg="yellow")
                            # "remove" WHERE the letter is in correctArr so that it is not counted again
                            # this is why we still have positionArr
                            correctArr[correctArr.index(word[i])] = "0" 
                            positionArr.append(i)
                for i in range(noLetters):
                    if i not in positionArr:   # ie. if the letter is not in the word
                        guessArray[self.guess_count][i].config(text = word[i], bg="light grey")

                self.guess_count += 1

                if word == correct_word:
                    status.config(text=f"Congratulations you got the word! You guessed the word in {self.guess_count} guesses!")
                if self.guess_count == maxGuesses:
                    status.config(text="Sorry, you ran out of guesses. The word was " + correct_word + ".")
            except ValueError as err:
                status.config(text=err)


        # frame where the guess attempt is received and where the guess is checked
        frameAttempt = tk.Frame(self)
        # status is for errors, congratulations and for running out of guesses
        status = tk.Label(frameAttempt, text="", wraplength=175)
        status.grid(row=0, column=0, padx=10, pady=(10,0))

        # where the guesses are made
        entryAttempt = tk.Entry(frameAttempt, width=25)
        entryAttempt.grid(row=1, column=0, padx=10, pady=10)

        # bind the enter key to the checkWord function. this is so that the user can press enter to submit the guess
        entryAttempt.bind('<Return>', checkWord)
        frameAttempt.grid(row=0, column=0)

        # frame where the guesses are kept in the colour boxes
        frameGuess = tk.Frame(self)

        ### all the guesses are stored in a 2D array called guessArray instead of creating 50 labels
        # 5 letter guesses across 10 guesses:
        guessArray = [[0]*noLetters for i in range(maxGuesses)]
        # i is the row (number of guesses), j is the column (letter in the guess)
        for i in range(maxGuesses):
            for j in range(noLetters):
                guessArray[i][j] = (tk.Label(frameGuess, text="", width=2, height=1, bg="grey", relief="solid"))
                guessArray[i][j].grid(row=i, column=j, padx=10, pady=10)

        frameGuess.grid(row=1, column=0)

        #lets you leave the game and go back to the welcome page
        #this will reset the guesses but not the correct word
        backButton = tk.Button(self, text="Back", width=8, command = self.on_back)
        backButton.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))

        self.pack()
    
    def on_back(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)  

window = tk.Tk()
window.geometry("500x400")

WelcomeWindow(window)
window.mainloop()