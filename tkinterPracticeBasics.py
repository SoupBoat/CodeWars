import tkinter as tk


# Create a window
window = tk.Tk()
window.title("My First GUI Program")
window.geometry("600x400")


# used frame1 and label1 to test locations
frame1 = tk.Frame(
    bg= "red",
    width=100,
    height=100
)
frame1.pack(fill=tk.BOTH, expand=True)   

label1 = tk.Label(
    master = frame1,
    text = "frame 1"
)
label1.pack()

# used fram2 and label2 to test locations
frame2 = tk.Frame(
    bg="blue"
)
frame2.pack(fill=tk.BOTH, expand=True)

label2 = tk.Label(
    master = frame2,
    bg="blue",
    fg="white",
    text = "frame 2"
)
# notice that I used place instead of pack
label2.place(anchor="center", relx=0.5, rely=0.5)  # this is used to place the label in the center of the frame2

# pack: is the simplest and most commonly used geometry manager. it organizes widgets in blocks before placing them
# place: uses coordinates instead 
# grid: organizes widgets in a table-like structure



# this function interacts with the input from the user
# it links within button in the command part. 
def checkWord():
    word = entry.get()
    lbl.config(text=word)

lbl = tk.Label(text="")
lbl.pack()

# Create a button to check whether the word is correct
button = tk.Button(
    master = frame1,    # sets which frame its in
    text="Check Word",
    width=25,
    height=5,
    bg="blue",  # shorthand for background
    fg="red",    # shorthand for foreground
    command=checkWord   # this is the function that will be called when the button is clicked
)
button.pack()

"""
tk.Entry    is a widget that allows the user to input a 
single line of text. It's useful when you want to accept 
simple, brief inputs from the user, like usernames, 
passwords, or short responses.

tk.Text     on the other hand, is a widget that allows 
the user to input multiple lines of text. It's useful 
when you want to accept larger inputs from the user, 
like paragraphs or blocks of code. the way you use .get() 
is different for Text and Entry
"""
entry = tk.Entry(
    width=50
)
entry.pack(pady=10)



# keep this at the end
window.mainloop()   # This will keep the window open until we close it