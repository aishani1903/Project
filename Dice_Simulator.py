#In this pgm I have created 2 dices out of which one is manipulated to give 6 often
import random
from tkinter import *

root = Tk()
root.title('Dice Simulator')
root.geometry('500x400')
label = Label(root, font = ('times', 250, 'bold'), text = '')
#func for unbiased dice
def roll_func():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']        #ascii value of symbols
    label.config(text=f'{random.choice(number)}')
    label.pack()
#func for biased dice
def roll_func2():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685','\u2685','\u2685','\u2685']        #ascii value of symbols
    label.config(text=f'{random.choice(number)}')
    label.pack()
#creating buttons
button = Button(root, font = ('helvetica', 25, 'bold'), text = 'Roll Dice', command = roll_func, bg = 'yellow')
button2 = Button(root, font = ('helvetica', 25, 'bold'), text = 'Roll Dice', command = roll_func2, bg = 'blue')
button.place(x = 330, y = 0)
button.pack()
button2.place(x = 300, y = 0)
button2.pack()
root.mainloop()
