from tkinter import *
from bin.gui.menu import _menu as main

def _gui():
    root = Tk()
    root.geometry('{}x{}'.format(1920, 1080))
    root.configure(background= "#a3e5ff")
    main(root)
    root.mainloop()
