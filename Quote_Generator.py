import tkinter as tk
import requests
from threading import Thread
api = "http://api.quotable.io/random"
quotes = []
quotes_number = 0

window = tk.Tk()
window.geometry("900x260")
window.title("Quotes Generator")
window.grid_columnconfigure(0,weight = 1)
window.resizable(False, False)     #ypou wont be able to stretch the window
window.configure(bg = "pink")

def get_random_qoute():
    pass

#UI
quote_label = tk.Label(window, text = "Click on the button to generate a random number",
                       height = 6,
                       pady = 10,
                       wraplength = 800,
                       font = ("Helvatica", 14))
quote_label.grid(row=0, column = 0, stick = "WE", padx = 20, pady = 10)

#button
button = tk.Button(test = "Generate", commannd = get_random_qoute, bg = "#0052cc", fg = "#ffffff",
                   activebackground = "grey", font = ("Helvatica", 14))
button.grid(row=0, column = 0, stick = "WE", padx = 20, pady = 10)

#executes the program
if __name__ == '__main__':
    window.mainloop()
