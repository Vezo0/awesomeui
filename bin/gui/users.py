from tkinter import *
import json
import sys

if __name__ == "__main__":
    _mod = sys.modules['users'] = sys.modules[__name__]

def change_users(frame,root):
    pass

def add_user_submit(name, prof, room,frame,root):
    frame.pack_forget()
    buffer = {}
    buffer[prof,room] = name
    with open("../json/data.json", "w") as jsonFile:
        data = json.load(jsonFile)
    data.append(buffer)
    _menu(root)

def add_user(frame,root):
    frame.pack_forget()
    frame_adduser = Frame(root)
    frame_adduser.pack(side=TOP)
    label1 = Label(frame_adduser,"Name: ")
    label2 = Label(frame_adduser,"Prof: ")
    label3 = Label(frame_adduser,"Room: ")
    entry1 = Entry(frame_adduser)
    entry2 = Entry(frame_adduser)
    entry3 = Entry(frame_adduser)
    button_submit = Button(frame_adduser,text="Submit", width=30,height=7,borderwidth=1,fg='black',background="#a3a5ff",command=lambda: add_user_submit(entry1,entry2,entry3,frame_adduser,root))
    label1.grid(row=0)
    label2.grid(row=1)
    label3.grid(row=2)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    entry3.grid(row=2, column=1)

def _user_menu(root):
    frame = Frame(root)
    frame.pack(side=TOP)
    user_button1 = Button(frame,text="Change users", width=70,height=7,borderwidth=1,fg='black',background="#a3a5ff",command=lambda: change_users(frame,root))
    user_button2 = Button(frame,text="Add user",width=70,height=7,borderwidth=1,fg='black',background="#a3a5ff",command=lambda: add_user(frame,root))
    user_button1.pack()
    user_button2.pack()