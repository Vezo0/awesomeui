from tkinter import *
from bin.gui.helpdesk import find_doc
from bin.gui.users import _user_menu

def m_doc(frame,root):
    frame.pack_forget()
    find_doc(root)


def _menu(root):
    root.title("Simple Prog")
    frame = Frame(root)
    frame.pack(side=TOP)
    menu_label = Label(frame,text="Welcome to menu", height=7,fg='black',background="#a3e5ff")
    menu_button1 = Button(frame,width=70,height=7,borderwidth=1,fg='black',background="#a3a5ff", text="helpdesk",command=lambda: m_doc(frame,root))
    menu_button2 = Button(frame,width=70,height=7,borderwidth=1,fg='black',background="#a3a5ff", text="User settings",command=lambda: _user_menu(frame,root))
    menu_label.pack(fill=X)
    menu_button1.pack()
    menu_button2.pack()

            
    
