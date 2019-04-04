from tkinter import *
from bin.gui.menu import _menu
import sys

if __name__ == "__main__":
    _mod = sys.modules['gui'] = sys.modules[__name__]
def _gui():
    root = Tk()
    root.geometry('{}x{}'.format(1920, 5080))
    root.configure(background= "#a3e5ff")
    _menu(root)
    root.mainloop()
