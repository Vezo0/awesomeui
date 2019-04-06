from bin.gui.alias import *
from tkinter import *
import json
from bin.custom.check import check_state
import bin.gui.menu as menu

json_path = "bin/json/data.json"
with open(json_path, "r") as json_read:
    data = json.load(json_read)
global idx, diction, tg
tg = 0
idx = 1
diction = {
    1:"Male",
    2:"Female",
    3:"Head",
    4:"Legs",
    5:"Stomach",
    6:"Chest",
    7:"Back",
    8:"Forehead",
    9:"Nose",
    10:"Ears",
    11:"Teeth",
    12:"Neck",
    13:"Eyes",
    14:"Back",
    15:"Heart", #m
    16:"Lungs",
    17:"Gullet",
    18:"Back",
    19:"Heart",
    20:"Lungs",
    21:"Gullet",
    22:"Breast",
    23:"Back",
}

def check():
    pass

def find_doc(rt):
    global fr1
    fr1 = rt
    buttons(fr1)
    
def to_surgeon(frame,root):
    global fr1
    buffer = dict()
    if check_state("surgeon") !="nokey":
        buffer.update(data[check_state("surgeon")])
        button_1.configure(text=surgeon, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.configure(text='Please, attach your ID card or contact with doctor in ROOM ' + buffer['room'], background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()
    elif check_state("surgeon") == "nokey":
        button_1.configure(text="Sorry, but we are on tea break, come later", background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.pack_forget()
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()

def to_therapist(frame,root):
    global fr1
    buffer = dict()
    buffer.update(data[check_state("therapist")])
    if check_state("therapist") !="nokey":
        button_1.configure(text=therapist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.configure(text='Please, attach your ID card or contact with doctor in ROOM ' + buffer['room'], background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()
    else:
        button_1.configure(text="Sorry, but we are on tea break, come later", background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.pack_forget()
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()

def to_stomatologist(frame,root):
    global fr1
    buffer = dict()
    if check_state("stomatologist") != "nokey":
        buffer.update(data[check_state("stomatologist")])
        button_1.configure(text=stomatologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.configure(text='Please, attach your ID card or contact with doctor in ROOM ' + buffer['room'], background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()
    else:
        button_1.configure(text="Sorry, but we are on tea break, come later", background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.pack_forget()
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()

def to_ophtalmologist(frame,root):
    global fr1
    buffer = dict()

    if check_state("ophtalmologist") !="nokey":
        buffer.update(data[check_state("ophtalmologist")])
        button_1.configure(text=ophtalmologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.configure(text='Please, attach your ID card or contact with doctor in ROOM ' + buffer['room'], background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()
    else:
        button_1.configure(text="Sorry, but we are on tea break, come later", background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.pack_forget()
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()

def to_cardiologist(frame,root):
    global fr1
    buffer = dict()
    
    if check_state("cardiologist") !="nokey":
        buffer.update(data[check_state("cardiologist")])
        button_1.configure(text=cardiologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.configure(text='Please, attach your ID card or contact with doctor in ROOM ' + buffer['room'], background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()
    else:
        button_1.configure(text="Sorry, but we are on tea break, come later", background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.pack_forget()
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()

def to_mammologist(frame,root):
    global fr1
    buffer = dict()
    
    if check_state("mammologist") !="nokey":
        buffer.update(data[check_state("mammologist")])
        button_1.configure(text=mammologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.configure(text='Please, attach your ID card or contact with doctor in ROOM ' + buffer['room'], background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()
    else:
        button_1.configure(text="Sorry, but we are on tea break, come later", background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
        button_2.pack_forget()
        button_3.pack_forget()
        button_4.pack_forget()
        button_5.pack_forget()
        button_6.pack_forget()
        button_7.pack_forget()
        button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
        button_back.pack()


def to_urologist(frame,root):
    global fr1
    button_1.configure(text=urologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
    button_2.pack_forget()
    button_3.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='Please, attach your ID card or contact with doctor. ROOM 412', background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
    button_5.pack_forget()
    button_6.pack_forget()
    button_7.pack_forget()
    button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
    button_back.pack()
    to_menu(frame,root)


def to_proctologist(frame,root):
    global fr1
    button_1.configure(text=proctologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
    button_2.pack_forget()
    button_3.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='Please, attach your ID card or contact with doctor. ROOM 424', background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
    button_5.pack_forget()
    button_6.pack_forget()
    button_7.pack_forget()
    button_back = Button(text="Back to menu", background="#a3a5ff",fg="black", borderwidth=1, width=70, height = 7, command=lambda: to_menu(frame,root,button_back))
    button_back.pack()
    to_menu(frame,root)
    label1 = Label(fr1, proctologist)
    label1.pack(side=TOP)

def click_d2(frame,root):
    global diction
    button_1.configure(text='Where hurts?', background="#a3e5ff",fg='black',borderwidth=0,state=DISABLED)
    button_2.configure(text='Sides', background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=lambda: to_cardiologist(frame,root))
    button_3.configure(text='Middle', background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=lambda:to_surgeon(frame,root))
    button_4.configure(text='I dont know', background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=lambda:to_surgeon(frame,root))
    button_5.configure(text='', background="#a3e5ff",fg='black',borderwidth=0,state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,state=DISABLED,fg="#a3e5ff")

def click_d(frame,root):
    global diction
    button_1.configure(text='Do you have a high preassure?', background="#a3e5ff",fg='black',borderwidth=0,state=DISABLED)
    button_2.configure(text='Yes', background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=lambda: to_cardiologist(frame,root))
    button_3.configure(text='No', background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=lambda:to_surgeon(frame,root))
    button_4.configure(text='I dont know', background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=lambda:click_d(frame,root))
    button_5.configure(text='', background="#a3e5ff",fg='black',borderwidth=0,state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,state=DISABLED,fg="#a3e5ff")

def click_f(frame,root):
    global diction
    idx=3
    button_1.configure(text=diction[idx], background="#a3a5ff",fg='black', command=lambda:click_h(frame,root))
    button_2.configure(text=diction[idx+1], background="#a3a5ff",fg='black', command=lambda:to_surgeon(frame,root))
    button_3.configure(text=diction[idx+2], background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=lambda:to_surgeon(frame,root))
    button_4.configure(text=diction[idx+3], background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=lambda:click_f(frame,root))
    button_5.configure(text=diction[idx+4], background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=lambda:click_s(fr1,root))
    button_6.configure(text='', background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,state=DISABLED,fg="#a3e5ff")

def click_s(frame,root):
    global diction, fr1
    idx = 1
    button_1.configure(text=diction[idx],background="#a3a5ff",borderwidth=1,fg='black',state="normal",width=70,height=7, command=lambda:click_m(frame,root))
    button_2.configure(text=diction[idx+1],background="#a3a5ff",borderwidth=1,fg='black',state="normal",width=70,height=7, command=lambda:click_f(frame,root))
    button_3.configure(text='',width=70,height=7,background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='',width=70,height=7,background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_5.configure(text='',width=70,height=7,background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_6.configure(text='',width=70,height=7,background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='',width=70,height=7,background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)

def click_m(frame,root):
    global diction, fr1
    idx=3
    button_1.configure(text=diction[idx], background="#a3a5ff",fg='black',state="normal", command=lambda:click_h(frame,root))
    button_2.configure(text=diction[idx+1], background="#a3a5ff",fg='black',state="normal", command=lambda:to_surgeon(frame,root))
    button_3.configure(text=diction[idx+2], background="#a3a5ff",borderwidth=1,fg='black',state="normal", command=lambda:to_surgeon(frame,root))
    button_4.configure(text=diction[idx+3], background="#a3a5ff",borderwidth=1,fg='black',state="normal", command=lambda:click_f(frame,root))
    button_5.configure(text=diction[idx+4], background="#a3a5ff",borderwidth=1,fg='black',state="normal", command=lambda:click_s(fr1,root))
    button_6.pack_forget()
    button_7.configure(text=' ', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)

def click_h(frame,root):
    global diction
    
    idx = 8
    button_1.configure(text=diction[idx], background="#a3a5ff",fg='black',state="normal",command=lambda:click_d(frame,root))
    button_2.configure(text=diction[idx+1],background="#a3a5ff",fg='black',state="normal",command=lambda:to_therapist(frame,root))
    button_3.configure(text=diction[idx+2],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=lambda:to_therapist(frame,root))
    button_4.configure(text=diction[idx+3],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=lambda:to_stomatologist(frame,root))
    button_5.configure(text=diction[idx+4],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=lambda:to_surgeon(frame,root))
    button_6.configure(text=diction[idx+5],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=lambda:to_ophtalmologist(frame,root))
    button_7.configure(text=diction[idx+6],background="#a3a5ff",borderwidth=1,fg='black',state="normal", command=lambda:click_m(frame,root))
    
def click_fc(frame,root):
    global diction
    idx = 19
    button_1.configure(text=diction[idx], background="#a3a5ff",fg='black',state="normal",command=lambda: to_cardiologist(frame,root))
    button_2.configure(text=diction[idx+1],background="#a3a5ff",fg='black',state="normal",command=lambda:to_surgeon(frame,root))
    button_3.configure(text=diction[idx+2],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=lambda:to_surgeon(frame,root))
    button_4.configure(text=diction[idx+3],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=lambda:to_mammologist(frame,root))
    button_5.configure(text=diction[idx+4],background="#a3a5ff",borderwidth=1,fg='black',state="normal", command=lambda:click_f(frame,root))
    button_6.configure(text='',background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='',background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)

def click_mc(frame,root):
    global diction
    idx = 15
    button_1.configure(text=diction[idx],background="#a3a5ff",fg='black',state="normal",command=lambda: to_cardiologist(frame,root))
    button_2.configure(text=diction[idx+1],background="#a3a5ff",fg='black',state="normal",command=lambda:to_surgeon(frame,root))
    button_3.configure(text=diction[idx+2],background="#a3a5ff",fg='black',state="normal",command=lambda:to_surgeon(frame,root))
    button_4.configure(text=diction[idx+3],background="#a3a5ff",fg='black',state="normal", command=lambda:click_m(frame,root))
    button_5.configure(text='',background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    button_6.configure(text='',background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    button_7.configure(text='',background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)

def buttons(root):
    global button_1, button_2, button_3, button_4,button_5,button_6,button_7,diction
    fr1 = Frame(root)
    fr1.pack(side=TOP)
    button_1 = Button(fr1,width=70,height=7,borderwidth=0,fg='#a3e5ff',background="#a3e5ff", text="",state=DISABLED)
    button_2 = Button(fr1,width=70,height=7,borderwidth=0,fg="black",background="#a3e5ff", text="Ochrana zdravotnictva.",state=DISABLED)
    button_3 = Button(fr1,width=70,height=7,borderwidth=0,fg="#a3e5ff", text='',background="#a3e5ff",state=DISABLED)
    button_4 = Button(fr1,width=70,height=7,borderwidth=1,fg="black", text='START',background="#a3a5ff",state="normal",command=lambda:click_s(fr1,root))
    button_5 = Button(fr1,width=70,height=7,borderwidth=0,fg="#a3e5ff", text='',background="#a3e5ff",state=DISABLED)
    button_6 = Button(fr1,width=70,height=7,borderwidth=0,fg="#000000", text='',background="#a3e5ff",state=DISABLED)
    button_7 = Button(fr1,width=70,height=7,borderwidth=0,fg="#a3e5ff", text='',background="#a3e5ff",state=DISABLED)
    button_1.pack(fill=X)
    button_2.pack(fill=X)
    button_3.pack(fill=X)
    button_4.pack(fill=X)
    button_5.pack(fill=X)
    button_6.pack(fill=X)
    button_7.pack(fill=X)

def to_menu(frame,root,button):
    button.pack_forget()
    frame.pack_forget()
    menu._menu(root)