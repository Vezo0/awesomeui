from tkinter import *


sex = 'Choose your sex'

segment = 'Which segment of body do you want to inspect?'

part = 'Which part of it do you want to inspect?'

exact = 'What exactly do you want to inspect?'

surgeon = 'You should go to surgeon. Please, select a suitable day and time for yourself.'

therapist = 'You should go to therapist. Please, select a suitable day and time for yourself.'

stomatologist = 'You should go to stomatologist. Please, select a suitable day and time for yourself.'

ophthalmologist = 'You should go to ophthalmologist. Please, select a suitable day and time for yourself.'

cardiologist = 'You should go to cardiologist. Please, select a suitable day and time for yourself.'

mammologist = 'You should go to mammologist. Please, select a suitable day and time for yourself.'

urologist = 'You should go to urologist. Please, select a suitable day and time for yourself.'

proctologist = 'You should go to proctologist. Please, select a suitable day and time for yourself.'

venerologist = 'You should go to venerologist. Please, select a suitable day and time for yourself.'

def hide(event):
    event.pack_forget()

def to_surgeon():
    global root
    button_1.configure(text=surgeon, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
    button_2.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_3.configure(text='', background="#a3e5ff",borderwidth=0,fg="black",state=DISABLED)
    button_4.configure(text='Please, attach your ID card or contact with doctor. ROOM 424', background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
    button_5.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)

def to_therapist():
    global root
    button_1.configure(text=therapist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
    button_2.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_3.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='Please, attach your ID card or contact with doctor. ROOM 401', background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
    button_5.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)

def to_stomatologist():
    global root
    button_1.configure(text=stomatologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
    button_2.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_3.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='Please, attach your ID card or contact with doctor. ROOM 317', background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
    button_5.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)

def to_ophtalmologist():
    global root
    button_1.configure(text=ophthalmologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
    button_2.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_3.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='Please, attach your ID card or contact with doctor. ROOM 124', background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
    button_5.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)

def to_cardiologist():
    global root
    button_1.configure(text=cardiologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
    button_2.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_3.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='Please, attach your ID card or contact with doctor. ROOM 133', background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
    button_5.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)

def to_mammologist():
    global root
    button_1.configure(text=mammologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
    button_2.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_3.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='Please, attach your ID card or contact with doctor. ROOM 332', background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
    button_5.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)


def to_urologist():
    global root
    button_1.configure(text=urologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
    button_2.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_3.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='Please, attach your ID card or contact with doctor. ROOM 412', background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
    button_5.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)


def to_proctologist():
    global root
    button_1.configure(text=proctologist, background="#a3e5ff", borderwidth=0, width=200,state=DISABLED, font=("Courier", 20), fg='black')
    button_2.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_3.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='Please, attach your ID card or contact with doctor. ROOM 424', background="#a3e5ff",borderwidth=0,width = 80,fg="black",state=DISABLED)
    button_5.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    label1 = Label(root, proctologist)
    label1.pack(side=TOP)

def click_d2():
    global diction, state
    button_1.configure(text='Where hurts?', background="#a3e5ff",fg='black',borderwidth=0, state=DISABLED)
    button_2.configure(text='Sides', background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=to_cardiologist)
    button_3.configure(text='Middle', background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=to_surgeon)
    button_4.configure(text='I dont know', background="#a3a5ff",fg='black',borderwidth=1, state="normal", command=to_surgeon)
    button_5.configure(text='', background="#a3e5ff",fg='black',borderwidth=0, state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,state=DISABLED,fg="#a3e5ff")

def click_d():
    global diction, state
    button_1.configure(text='Do you have a high preassure?', background="#a3e5ff",fg='black',borderwidth=0, state=DISABLED)
    button_2.configure(text='Yes', background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=to_cardiologist)
    button_3.configure(text='No', background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=to_surgeon)
    button_4.configure(text='I dont know', background="#a3a5ff",fg='black',borderwidth=1, state="normal", command=click_d2)
    button_5.configure(text='', background="#a3e5ff",fg='black',borderwidth=0, state=DISABLED)
    button_6.configure(text='', background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,state=DISABLED,fg="#a3e5ff")

def click_f():
    global diction, state
    idx=3
    button_1.configure(text=diction[idx], background="#a3a5ff",fg='black', command=click_h)
    button_2.configure(text=diction[idx+1], background="#a3a5ff",fg='black', command=to_surgeon)
    button_3.configure(text=diction[idx+2], background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=to_surgeon)
    button_4.configure(text=diction[idx+3], background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=click_fc)
    button_5.configure(text=diction[idx+4], background="#a3a5ff",fg='black',borderwidth=1,state="normal", command=click_s)
    button_6.configure(text='', background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,state=DISABLED,fg="#a3e5ff")

def click_s():
    global diction, state, root
    idx = 1
    button_1.configure(text=diction[idx],background="#a3a5ff",borderwidth=1,fg='black',state="normal",width=70,height=7, command=click_m)
    button_2.configure(text=diction[idx+1],background="#a3a5ff",borderwidth=1,fg='black',state="normal",width=70,height=7, command=click_f)
    button_3.configure(text='',width=70,height=7,background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_4.configure(text='',width=70,height=7,background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_5.configure(text='',width=70,height=7,background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_6.configure(text='',width=70,height=7,background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='',width=70,height=7,background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)

def click_m():
    global diction, state, root
    idx=3
    button_1.configure(text=diction[idx], background="#a3a5ff",fg='black',state="normal", command=click_h)
    button_2.configure(text=diction[idx+1], background="#a3a5ff",fg='black',state="normal", command=to_surgeon)
    button_3.configure(text=diction[idx+2], background="#a3a5ff",borderwidth=1,fg='black',state="normal", command=to_surgeon)
    button_4.configure(text=diction[idx+3], background="#a3a5ff",borderwidth=1,fg='black',state="normal", command=click_fc)
    button_5.configure(text=diction[idx+4], background="#a3a5ff",borderwidth=1,fg='black',state="normal", command=click_s)
    button_6.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff", state=DISABLED)
    button_7.configure(text='', background="#a3e5ff",borderwidth=0,fg="#a3e5ff", state=DISABLED)
    state.append(1) 
    print(state)

def click_h():
    global diction, state
    
    idx = 8
    button_1.configure(text=diction[idx], background="#a3a5ff",fg='black',state="normal",command=click_d)
    button_2.configure(text=diction[idx+1],background="#a3a5ff",fg='black',state="normal",command=to_therapist)
    button_3.configure(text=diction[idx+2],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=to_therapist)
    button_4.configure(text=diction[idx+3],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=to_stomatologist)
    button_5.configure(text=diction[idx+4],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=to_surgeon)
    button_6.configure(text=diction[idx+5],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=to_ophtalmologist)
    button_7.configure(text=diction[idx+6],background="#a3a5ff",borderwidth=1,fg='black',state="normal", command=click_m)
    state.append(3)
    

def click_fc():
    global diction, state
    
    idx = 19
    button_1.configure(text=diction[idx], background="#a3a5ff",fg='black',state="normal",command=to_cardiologist)
    button_2.configure(text=diction[idx+1],background="#a3a5ff",fg='black',state="normal",command=to_surgeon)
    button_3.configure(text=diction[idx+2],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=to_surgeon)
    button_4.configure(text=diction[idx+3],background="#a3a5ff",borderwidth=1,fg='black',state="normal",command=to_mammologist)
    button_5.configure(text=diction[idx+4],background="#a3a5ff",borderwidth=1,fg='black',state="normal", command=click_f)
    button_6.configure(text='',background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    button_7.configure(text='',background="#a3e5ff",borderwidth=0,fg="#a3e5ff",state=DISABLED)
    state = 4

def click_mc():
    global diction, state
    
    idx = 15
    button_1.configure(text=diction[idx],background="#a3a5ff",fg='black',state="normal",command=to_cardiologist)
    button_2.configure(text=diction[idx+1],background="#a3a5ff",fg='black',state="normal",command=to_surgeon)
    button_3.configure(text=diction[idx+2],background="#a3a5ff",fg='black',state="normal",command=to_surgeon)
    button_4.configure(text=diction[idx+3],background="#a3a5ff",fg='black',state="normal", command=click_m)
    button_5.configure(text='',background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    button_6.configure(text='',background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    button_7.configure(text='',background="#a3e5ff",fg="#a3e5ff",borderwidth=0,state=DISABLED)
    state = 5

def buttons(root):
    global button_1, button_2, button_3, button_4,button_5,button_6,button_7,diction
    fr1 = Frame(root)
    fr1.pack(side=TOP)
    print(state)
    if state[-1] == 0:
        button_1 = Button(fr1,width=70,height=7,borderwidth=0,fg='#a3e5ff',background="#a3e5ff", text="",state=DISABLED)
        button_2 = Button(fr1,width=70,height=7,borderwidth=0,fg="black",background="#a3e5ff", text="Ochrana zdravotnictva.", state=DISABLED)
        button_3 = Button(fr1,width=70,height=7,borderwidth=0,fg="#a3e5ff", text='',background="#a3e5ff",state=DISABLED)
        button_4 = Button(fr1,width=70,height=7,borderwidth=1,fg="black", text='START',background="#a3a5ff",state="normal",command=click_s)
        button_5 = Button(fr1,width=70,height=7,borderwidth=0,fg="#a3e5ff", text='',background="#a3e5ff",state=DISABLED)
        button_6 = Button(fr1,width=70,height=7,borderwidth=0,fg="#000000", text='',background="#a3e5ff",state=DISABLED)
        button_7 = Button(fr1,width=70,height=7,borderwidth=0,fg="#a3e5ff", text='',background="#a3e5ff",state=DISABLED)
        button_1.pack()
        button_2.pack(fill=X)
        button_3.pack(fill=X)
        button_4.pack(fill=X)
        button_5.pack(fill=X)
        button_6.pack(fill=X)
        button_7.pack(fill=X)
    
if __name__ == "__main__":
    global idx, state, diction, tg
    tg = 0
    state = []
    state.append(0)
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


root = Tk()
root.geometry('{}x{}'.format(1920, 5080))
root.configure(background= "#a3e5ff")
buttons(root)
root.mainloop()

