import tkinter as tk

win=tk.Tk()

def hendle_keypress(event):
    """Выводит символ, связанный с нажатой клавишей"""
    print(event.char)
win.mainloop()
