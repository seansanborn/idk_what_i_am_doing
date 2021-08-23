
import string
from random import *

# password generator
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(randint(16, 32)))

import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=5, width=30, font=("timesnewroman", 32))
T.pack()
quote = (password)
T.insert(tk.END, quote)
tk.mainloop()