from tkinter import *

def click():
    global state, diction_sex, diction_femalechest, diction_femaleintimate, diction_head, diction_main, diction_malechest, diction_maleintimate
    if state == 0:
        button_1.configure(text=diction_sex[1],background='black')
        button_2.configure(text=diction_sex[2],background='black')
        button_3.configure(text=diction_sex[1],background='turquoise')
        button_4.configure(text=diction_sex[1],background='turquoise')
        button_5.configure(text=diction_sex[1],background='turquoise')
        button_6.configure(text=diction_sex[1],background='turquoise')
        button_7.configure(text=diction_sex[1],background='turquoise')
        state = 1
    elif state == 1:
        button_1.configure(text=diction_main[1], background='black',fg='red')
        button_2.configure(text=diction_main[2],background='black',fg='red')
        button_3.configure(text=diction_main[3],background='black',fg='red')
        button_4.configure(text=diction_main[4],background='black',fg='red')
        button_5.configure(text=diction_main[5],background='black',fg='red')
        button_6.configure(text=diction_main[6],background='black',fg='red')
        button_7.configure(text=diction_main[7],background='black',fg='red')
        state=2
    elif state == 2:
        button_1.configure(text=diction_head[1], background='black',fg='red')
        button_2.configure(text=diction_head[2],background='black',fg='red')
        button_3.configure(text=diction_head[3],background='black',fg='red')
        button_4.configure(text=diction_head[4],background='black',fg='red')
        button_5.configure(text=diction_head[5],background='black',fg='red')
        button_6.configure(text=diction_head[6],background='black',fg='red')
        button_7.configure(text=diction_head[7],background='black',fg='red')

def buttons(root):
    global state, button_1, button_2, button_3, button_4,button_5,button_6,button_7,diction_sex, diction_femalechest, diction_femaleintimate, diction_head, diction_main, diction_malechest, diction_maleintimate
    fr1 = Frame(root)
    fr1.pack(side=LEFT)
    if state == 0:
        button_1 = Button(fr1,text=diction_sex[1], command=click)
        button_2 = Button(fr1,text=diction_sex[2], command=click)
        button_3 = Button(fr1,text=diction_sex[1], command=click)
        button_4 = Button(fr1,text=diction_sex[2], command=click)
        button_5 = Button(fr1,text=diction_sex[1], command=click)
        button_6 = Button(fr1,text=diction_sex[2], command=click)
        button_7 = Button(fr1,text=diction_sex[1], command=click)
        button_1.pack()
        button_2.pack()
        button_3.pack()
        button_4.pack()
        button_5.pack()
        button_6.pack()
        button_7.pack()
        
    elif state == 1:
        button_1 = Button(fr1,text=diction_main[1], command=click)
        button_2 = Button(fr1,text=diction_main[2], command=click)
        button_3 = Button(fr1,text=diction_main[3], command=click)
        button_4 = Button(fr1,text=diction_main[4], command=click)
        button_5 = Button(fr1,text=diction_main[5], command=click)
        button_6 = Button(fr1,text=diction_main[6], command=click)
        button_7 = Button(fr1,text=diction_main[7], command=click)
        button_1.pack()
        button_2.pack()
        button_3.pack()
        button_4.pack()
        button_5.pack()
        button_6.pack()
        button_7.pack()
        
    #head
    elif state == 2:
        button_1 = Button(fr1,text=diction_head[1], command=click)
        button_2 = Button(fr1,text=diction_head[2], command=click)
        button_3 = Button(fr1,text=diction_head[3], command=click)
        button_4 = Button(fr1,text=diction_head[4], command=click)
        button_5 = Button(fr1,text=diction_head[5], command=click)
        button_6 = Button(fr1,text=diction_head[6], command=click)
        button_7 = Button(fr1,text=diction_head[7], command=click)
        button_1.pack()
        button_2.pack()
        button_3.pack()
        button_4.pack()
        button_5.pack()
        button_6.pack()
        button_7.pack()

if __name__ == "__main__":
    global state, diction_sex, diction_main, diction_head, diction_malechest, diction_femalechest, diction_maleintimate, diction_femaleintimate
    state = 0

    diction_sex = {
    1:"Male",
    2:"Female",
}
    diction_main = {
    1:"Head",
    2:"Chest",
    3:"Hands",
    4:"Legs",
    5:"Stomach",
    6:"Intimate zones",
    7:"Back",
}
    diction_head = {
    1:"Forehead",
    2:"Nose",
    3:"Ears",
    4:"Teeth",
    5:"Neck",
    6:"Eyes",
    7:"Back",
}
    diction_malechest = {
    1:"Heart",
    2:"Lungs",
    3:"Gullet",
    4:"Back",
}
    diction_femalechest = {
    1:"Heart",
    2:"Lungs",
    3:"Gullet",
    4:"Breast",
    5:"Back",
}
    diction_maleintimate = {
    1:"Penis",
    2:"Butt",
    3:"Back",
}
    diction_femaleintimate = {
    1:"Vagina",
    2:"Butt",
    3:"Back",
}

root = Tk()
buttons(root)
click()
root.mainloop()