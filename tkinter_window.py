from tkinter import *
from random import randint
import random
 
root = Tk()
root.title('PinPassGen 1.5')
root.geometry("500x300")
root.configure(bg="lightgrey")
app_width = 500
app_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')





 
root.mainloop()
