import tkinter 
import somefunc 

tg = 0
l = []

def OnButtonClick(theGrid, button_id):
    #sex
    if button_id == 1 and len(l) == 0:
        l.append("male")
        l.append("malefemale")
    elif button_id == 2 and len(l) == 0:
        l.append("female")
        l.append("malefemale")
    #head
    elif button_id == 1 and l[-1] == "malefemale":
        l.append("malefemalehead")
    elif button_id == 1 and l[-1] == "malefemalehead":
        tg = 1
    elif button_id == 2 and l[-1] == "malefemalehead":
        tg = 1
    elif button_id == 3 and l[-1] == "malefemalehead":
        tg = 1
    elif button_id == 4 and l[-1] == "malefemalehead":
        tg = 1
    elif button_id == 5 and l[-1] == "malefemalehead":
        tg = 1
    elif button_id == 6 and l[-1] == "malefemalehead":
        tg = 1
    #malechest
    elif button_id == 2 and l[0] == "male":
        l.append("malechest")
    elif button_id == 1 and l[-1] == "malechest":
        tg = 1
    elif button_id == 2 and l[-1] == "malechest":
        tg = 1
    elif button_id == 3 and l[-1] == "malechest":
        tg = 1
    #femalechest
    elif button_id == 2 and l[0] == "female":
        l.append("femalechest")
    elif button_id == 1 and l[-1] == "femalechest":
        tg = 1
    elif button_id == 2 and l[-1] == "femalechest":
        tg = 1
    elif button_id == 3 and l[-1] == "femalechest":
        tg = 1
    elif button_id == 4 and l[-1] == "femalechest":
        tg = 1
    #hands
    elif button_id == 3 and l[0] == "male":
        tg = 1
    elif button_id == 3 and l[0] == "female":
        tg = 1
    #legs
    elif button_id == 4 and l[0] == "male":
        tg = 1
    elif button_id == 4 and l[0] == "female":
        tg = 1
    #stomach
    elif button_id == 5 and l[0] == "male":
        tg = 1
    elif button_id == 5 and l[0] == "female":
        tg = 1
    #intimate zones (M)
    elif button_id == 6 and l[0] == "male":
        l.append("maleintimate")
    elif button_id == 1 and l[-1] == "maleintimate":
        tg = 1
    elif button_id == 2 and l[-1] == "maleintimate":
        tg = 1
    #intimate zones (M)
    elif button_id == 6 and l[0] == "female":
        l.append("femaleintimate")
    elif button_id == 1 and l[-1] == "femaleintimate":
        tg = 1
    elif button_id == 2 and l[-1] == "femaleintimate":
        tg = 1   
    #back
    elif button_id == 7 and l[-1] == "malefemale":
        del l[-1]
    elif button_id == 7 and l[-1] == "malefemalehead":
        del l[-1]
    elif button_id == 7 and l[-1] == "malechest":
        del l[-1]
    elif button_id == 7 and l[-1] == "femalechest":
        del l[-1]
    elif button_id == 7 and l[-1] == "maleintimate":
        del l[-1]
    elif button_id == 7 and l[-1] == "femaleintimate":
        del l[-1]

from functools import partial
        

def createButtons(s, theGrid):
    if s is "sex":
        button1 = Button(theGrid, text="Male",padx=20,pady=20, fg="black", command=lambda: theGrid.OnButtonClick(1))
        button2 = Button(theGrid, text="Female",padx=20,pady=20, fg="black", command=lambda: theGrid.OnButtonClick(2))
    elif s is "malefemale":
        button1 = Button(theGrid, text="Head",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(1))
        button2 = Button(theGrid, text="Chest",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(2))
        button3 = Button(theGrid, text="Hands",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(3))
        button4 = Button(theGrid, text="Legs",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(4))
        button5 = Button(theGrid, text="Stomach",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(5))
        button6 = Button(theGrid, text="Intimate zones",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(6))
        buttonback = Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(7))
    elif s is "malefemalehead":
        button1 = Button(theGrid, text="Forehead",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(1)) #hir
        button2 = Button(theGrid, text="Nose",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(2)) #lor
        button3 = Button(theGrid, text="Ears",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(3)) #lor
        button4 = Button(theGrid, text="Teeth",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(4)) #st
        button5 = Button(theGrid, text="Neck",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(5)) #lor
        button6 = Button(theGrid, text="Eyes",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(6)) #ok
        buttonback = Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(7))
    elif s is "malechest":
        button1 = Button(theGrid, text="Heart",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(1)) #card
        button2 = Button(theGrid, text="Lungs",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(2)) #hir
        button3 = Button(theGrid, text="Gullet",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(3)) #hir
        buttonback = Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(7))
    elif s is "femalechest":
        button1 = Button(theGrid, text="Heart",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(1)) #card
        button2 = Button(theGrid, text="Lungs",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(2)) #hir
        button3 = Button(theGrid, text="Gullet",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(3)) #hir
        button4 = Button(theGrid, text="Breast",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(4))  #mom
        buttonback = Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(7))
    elif s is "maleintimate":
        button1 = Button(theGrid, text="Penis",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(1)) #ur
        button2 = Button(theGrid, text="Butt",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(2)) #pr
        buttonback = Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(7))
    elif s is "femaleintimate":
        button1 = Button(theGrid, text="Vagina",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(1)) #vin
        button2 = Button(theGrid, text="Butt",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(2)) #pr
        buttonback = Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: theGrid.OnButtonClick(7))
    

def createGrid():
    root = Tk()
    while tg is not 1:
        createButtons(l[-1], root)
        root.pack()
    root.mainloop()


