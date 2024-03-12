"""
This code below isa an edited verison of the code from 

https://coderslegacy.com/switching-between-multiple-screens-pages-in-tkinter/
January 6, 2024 by Siddiqi

The original code can be found at the link above and a youtube video explaining 
the code can be found there too.

I edited it to be different and added comments where I needed them.
Places wihtout comments either have explanations in tkinterPracticeBasics.py or
because i didn't understand what was happening in the code. 

"""

import tkinter as tk

# this function is used to center the window
def center_window(width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')


class WelcomeWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Welcome")
        center_window(200, 150)
        
        login_button = tk.Button(self, text="Login", width=10, command = self.on_login)
        login_button.pack(padx=20, pady=(20, 10)) # the 20 is above and the 10 is below
        
        register_button = tk.Button(self, text="Register", width=10, command = self.on_register)
        register_button.pack(pady=10)
        self.pack()

    def on_login(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        LoginWindow(self.master)

    def on_register(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        RegisterWindow(self.master)



class LoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Login")
        self.master.resizable(False, False)
        center_window(250, 150)
        
        tk.Label(self, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        
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
        MainWindow(self.master)       

        
class RegisterWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Register")
        self.master.resizable(False, False)
        center_window(300, 250)
        
        tk.Label(self, text="First Name:").grid(row=0, column=0, sticky="w")
        self.first_name_entry = tk.Entry(self, width=26)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        
        tk.Label(self, text="Last Name:").grid(row=1, column=0, sticky="w")
        self.last_name_entry = tk.Entry(self, width=26)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        
        tk.Label(self, text="Password:").grid(row=2, column=0, sticky="w")
        self.password_entry = tk.Entry(self, show="*", width=26)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")
        
        tk.Label(self, text="Email:").grid(row=3, column=0, sticky="w")
        self.email_entry = tk.Entry(self, width=26)
        self.email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        
        submit_button = tk.Button(self, text="Submit", width=8)
        submit_button.grid(row=7, column=1, padx=10, pady=10, sticky="e")

        submit_button = tk.Button(self, text="Back", width=8, command = self.on_back)
        submit_button.grid(row=7, column=0, sticky="w", padx=10, pady=(10, 10))
        self.pack()

    def on_back(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        center_window(500, 500)
        self.pack()     

root = tk.Tk()
root.eval('tk::PlaceWindow . center')   # this is used to center the window in tkinters base language
WelcomeWindow(root)
root.mainloop()