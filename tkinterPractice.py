import tkinter as tk


# Create a window
window = tk.Tk()
window.title("My First GUI Program")
window.geometry("400x200")

frame1 = tk.Frame(
    bg= "red",
    width=100,
    height=100
)
frame1.pack()

label1 = tk.Label(
    master = frame1,
    text = "frame 1"
)
label1.pack()


frame2 = tk.Frame(
    bg="blue"
)
frame2.pack()

label2 = tk.Label(
    master = frame2,
    text = "frame 2"
)
label2.pack()


## not needed for wordle yet
# greeting = tk.Label(
#     text="Hello, Tkinter",
#     foreground="white",  # Set the text color to white
#     background="black",  # Set the background color to black
#     )
# greeting.pack()  # This line will add the label to the window

def checkWord():
    word = entry.get()
    lbl.config(text=word)


lbl = tk.Label(text="")
lbl.pack()

# Create a button
button = tk.Button(
    master = frame1,
    text="Check Word",
    width=25,
    height=5,
    bg="blue",  # shorthand for background
    fg="red",    # shorthand for foreground
    command=checkWord
)
#button.pack()

##tk.Entry is a widget that allows the user to input a 
#single line of text. It's useful when you want to accept 
#simple, brief inputs from the user, like usernames, 
#passwords, or short responses.
##tk.Text, on the other hand, is a widget that allows 
#the user to input multiple lines of text. It's useful 
#when you want to accept larger inputs from the user, 
#like paragraphs or blocks of code.
entry = tk.Entry(
    width=50
    )
entry.pack()

name = entry.get()
tk.Label(text=name).pack()


# keep this at the end
window.mainloop()   # This will keep the window open until we close it