from tkinter import *
import bin.gui.menu as back_from_users
import json

json_path = "bin/json/data.json"

def change_state(buffer):
    if buffer['state'] == True:
        buffer['state'] = False
    else:
        buffer['state'] = True

def change_users_submit(frame,root,buffer):
    with open(json_path, "w") as json_write:
        json.dump(buffer,json_write,indent=4)
    frame.pack_forget()
    back_from_users._menu(root)

def set_idx_by_10(idx,frame,buffer,root):
    idx=idx-10
    frame.pack_forget()
    frame_changeusers = Frame(root)
    frame_changeusers.pack(side=TOP)
    buffer = dict()
    with open(json_path, "r") as json_read:
        data = json.load(json_read)
        buffer.update(data)
    set_states(idx,frame_changeusers,buffer)
    button_submit_change = Button(frame_changeusers,text="Submit",borderwidth=1,fg='black',background="#a3a5ff",command=lambda: change_users_submit(frame_changeusers,root,buffer))
    if len(buffer.keys()) > idx+10:
        button_next_page = Button(frame_changeusers,text="Next page", borderwidth=1,fg='black',background="#a3a5ff",command=lambda: set_idx_to_10(idx,frame_changeusers,buffer,root))
        button_next_page.pack()
    if idx>=10:
        button_back_page = Button(frame_changeusers,text="Back", borderwidth=1,fg='black',background="#a3a5ff",command=lambda: set_idx_by_10(idx,frame_changeusers,buffer,root))
        button_back_page.pack()
    button_back = Button(frame_changeusers,text="Back", borderwidth=1,fg='black',background="#a3a5ff",command=lambda:_user_menu(frame_changeusers, root))
    button_submit_change.pack()  
    button_back.pack()

def set_idx_to_10(idx,frame,buffer,root):
    idx=idx+10
    frame.pack_forget()
    frame_changeusers = Frame(root)
    frame_changeusers.pack(side=TOP)
    buffer = dict()
    with open(json_path, "r") as json_read:
        data = json.load(json_read)
        buffer.update(data)
    set_states(idx,frame_changeusers,buffer)
    button_submit_change = Button(frame_changeusers,text="Submit",borderwidth=1,fg='black',background="#a3a5ff",command=lambda: change_users_submit(frame_changeusers,root,buffer))
    if len(buffer.keys()) > idx+10:
        button_next_page = Button(frame_changeusers,text="Next page", borderwidth=1,fg='black',background="#a3a5ff",command=lambda: set_idx_to_10(idx,frame_changeusers,buffer,root))
        button_next_page.pack()
    if idx>=10:
        button_back_page = Button(frame_changeusers,text="Back", borderwidth=1,fg='black',background="#a3a5ff",command=lambda: set_idx_by_10(idx,frame_changeusers,buffer,root))
        button_back_page.pack()
    button_back = Button(frame_changeusers,text="Back", borderwidth=1,fg='black',background="#a3a5ff",command=lambda:_user_menu(frame_changeusers, root))
    button_submit_change.pack()  
    button_back.pack()

def check_state(buffer):
    if buffer["state"] == True:
        return 1
    else:
        return 0

def set_states(idx,frame_changeusers,buffer):
    check = Checkbutton(frame_changeusers,text=buffer[str(idx)],variable=check_state(buffer[str(idx)]), command=lambda: change_state(buffer[str(idx)]))
    check.pack()
    check.select()
    if len(buffer.keys()) > idx+1:
        Checkbutton(frame_changeusers,text=buffer[str(idx+1)],variable=check_state(buffer[str(idx+1)]), command=lambda: change_state(buffer[str(idx+1)])).pack()
        if len(buffer.keys()) > idx+2:
            Checkbutton(frame_changeusers,text=buffer[str(idx+2)],variable=check_state(buffer[str(idx+2)]), command=lambda: change_state(buffer[str(idx+2)])).pack()
            if len(buffer.keys()) > idx+3:
                Checkbutton(frame_changeusers,text=buffer[str(idx+3)],variable=check_state(buffer[str(idx+3)]), command=lambda: change_state(buffer[str(idx+3)])).pack()
                if len(buffer.keys()) > idx+4:
                    Checkbutton(frame_changeusers,text=buffer[str(idx+4)],variable=check_state(buffer[str(idx+4)]), command=lambda: change_state(buffer[str(idx+4)])).pack()
                    if len(buffer.keys()) > idx+5:
                        Checkbutton(frame_changeusers,text=buffer[str(idx+5)],variable=check_state(buffer[str(idx+5)]), command=lambda: change_state(buffer[str(idx+5)])).pack()
                        if len(buffer.keys()) > idx+6:
                            Checkbutton(frame_changeusers,text=buffer[str(idx+6)],variable=check_state(buffer[str(idx+6)]), command=lambda: change_state(buffer[str(idx+6)])).pack()
                            if len(buffer.keys()) > idx+7:
                                Checkbutton(frame_changeusers,text=buffer[str(idx+7)],variable=check_state(buffer[str(idx+7)]), command=lambda: change_state(buffer[str(idx+7)])).pack()
                                if len(buffer.keys()) > idx+8:
                                    Checkbutton(frame_changeusers,text=buffer[str(idx+8)],variable=check_state(buffer[str(idx+8)]), command=lambda: change_state(buffer[str(idx+8)])).pack()
                                    if len(buffer.keys()) > idx+9:
                                        Checkbutton(frame_changeusers,text=buffer[str(idx+9)],variable=check_state(buffer[str(idx+9)]), command=lambda: change_state(buffer[str(idx+9)])).pack()
def change_users(frame,root):
    frame.pack_forget()
    frame_changeusers = Frame(root)
    frame_changeusers.pack(side=TOP)
    buffer = dict()
    with open(json_path, "r") as json_read:
        data = json.load(json_read)
        buffer.update(data)
    idx=0
    set_states(idx,frame_changeusers,buffer)
    button_submit_change = Button(frame_changeusers,text="Submit",borderwidth=1,fg='black',background="#a3a5ff",command=lambda: change_users_submit(frame_changeusers,root,buffer))
    if len(buffer.keys()) > idx+10:
        button_next_page = Button(frame_changeusers,text="Next page", borderwidth=1,fg='black',background="#a3a5ff",command=lambda: set_idx_to_10(idx,frame_changeusers,buffer,root))
        button_next_page.pack()
    if idx>=10:
        button_back_page = Button(frame_changeusers,text="Back", borderwidth=1,fg='black',background="#a3a5ff",command=lambda: set_idx_by_10(idx,frame_changeusers,buffer,root))
        button_back_page.pack()
    button_back = Button(frame_changeusers,text="Back", borderwidth=1,fg='black',background="#a3a5ff",command=lambda:_user_menu(frame_changeusers, root))
    button_submit_change.pack()  
    button_back.pack()
    
def add_user_submit(name, prof, room,frame,root):
    n=name.get()
    p=prof.get()
    r=room.get()
    buffer = dict()
    with open(json_path, "r") as json_read:
        data = json.load(json_read)
        buffer.update(data)
        buffer[len(buffer.keys())] = {"name": n,"profession": p, "room": r, "state": True}
    with open(json_path, "w") as json_write:
        json.dump(buffer,json_write,indent=4)
    add_user(frame,root)

def add_user(frame,root):
    frame.pack_forget()
    frame_adduser = Frame(root)
    frame_adduser.pack(side=TOP)
    label1 = Label(frame_adduser,text="Name: ",fg="black")
    label2 = Label(frame_adduser,text="Prof: ",fg="black")
    label3 = Label(frame_adduser,text="Room: ",fg="black")
    entry1 = Entry(frame_adduser)
    entry2 = Entry(frame_adduser)
    entry3 = Entry(frame_adduser)
    button_submit = Button(frame_adduser,text="Submit", borderwidth=1,fg='black',background="#a3a5ff",command=lambda: add_user_submit(entry1,entry2,entry3,frame_adduser,root))
    button_back = Button(frame_adduser,text="Back", borderwidth=1,fg='black',background="#a3a5ff",command=lambda: _user_menu(frame_adduser,root))
    label1.grid(row=0)
    label2.grid(row=1)
    label3.grid(row=2)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    entry3.grid(row=2, column=1)
    button_submit.grid(row=3)
    button_back.grid(row=3,column=1)

def _user_menu(frame,root):
    frame.pack_forget()
    frame_usermenu = Frame(root)
    frame_usermenu.pack(side=TOP)
    user_button1 = Button(frame_usermenu,text="Change users", width=70,height=7,borderwidth=1,fg='black',background="#a3a5ff",command=lambda: change_users(frame_usermenu,root))
    user_button2 = Button(frame_usermenu,text="Add user",width=70,height=7,borderwidth=1,fg='black',background="#a3a5ff",command=lambda: add_user(frame_usermenu,root))
    user_button3 = Button(frame_usermenu,text="Back",width=70,height=7,borderwidth=1,fg='black',background="#a3a5ff",command=lambda: back_to_menu(frame_usermenu,root))
    user_button1.pack()
    user_button2.pack()
    user_button3.pack()

def back_to_menu(frame,root):
    frame.pack_forget()
    back_from_users._menu(root)