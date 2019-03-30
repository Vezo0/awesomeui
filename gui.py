from tkinter import *

tg = 0
l = []
l.append("sex")

def OnButtonClick(theGrid, button_id):
    #sex
    if button_id == 1 and l[0] == "sex":
        l[0] = "male"
        l.append("malefemale")
        theGrid.pack_forget()
    elif button_id == 2 and l[0] == "sex":
        l[0] = "female"
        l.append("malefemale")
        theGrid.pack_forget()
    #head
    elif button_id == 1 and l[-1] == "malefemale":
        l.append("malefemalehead")
        theGrid.pack_forget()
    elif button_id == 1 and l[-1] == "malefemalehead":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 2 and l[-1] == "malefemalehead":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 3 and l[-1] == "malefemalehead":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 4 and l[-1] == "malefemalehead":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 5 and l[-1] == "malefemalehead":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 6 and l[-1] == "malefemalehead":
        tg = 1
        theGrid.pack_forget()
    #malechest
    elif button_id == 2 and l[0] == "male":
        l.append("malechest")
        theGrid.pack_forget()
    elif button_id == 1 and l[-1] == "malechest":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 2 and l[-1] == "malechest":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 3 and l[-1] == "malechest":
        tg = 1
        theGrid.pack_forget()
    #femalechest
    elif button_id == 2 and l[0] == "female":
        l.append("femalechest")
        theGrid.pack_forget()
    elif button_id == 1 and l[-1] == "femalechest":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 2 and l[-1] == "femalechest":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 3 and l[-1] == "femalechest":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 4 and l[-1] == "femalechest":
        tg = 1
        theGrid.pack_forget()
    #hands
    elif button_id == 3 and l[0] == "male":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 3 and l[0] == "female":
        tg = 1
        theGrid.pack_forget()
    #legs
    elif button_id == 4 and l[0] == "male":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 4 and l[0] == "female":
        tg = 1
        theGrid.pack_forget()
    #stomach
    elif button_id == 5 and l[0] == "male":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 5 and l[0] == "female":
        tg = 1
        theGrid.pack_forget()
    #intimate zones (M)
    elif button_id == 6 and l[0] == "male":
        l.append("maleintimate")
        theGrid.pack_forget()
    elif button_id == 1 and l[-1] == "maleintimate":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 2 and l[-1] == "maleintimate":
        tg = 1
        theGrid.pack_forget()
    #intimate zones (M)
    elif button_id == 6 and l[0] == "female":
        l.append("femaleintimate")
        theGrid.pack_forget()
    elif button_id == 1 and l[-1] == "femaleintimate":
        tg = 1
        theGrid.pack_forget()
    elif button_id == 2 and l[-1] == "femaleintimate":
        tg = 1   
        theGrid.pack_forget()
    #back
    elif button_id == 7 and l[-1] == "malefemale":
        del l[-1]
        theGrid.pack_forget()
    elif button_id == 7 and l[-1] == "malefemalehead":
        del l[-1]
        theGrid.pack_forget()
    elif button_id == 7 and l[-1] == "malechest":
        del l[-1]
        theGrid.pack_forget()
    elif button_id == 7 and l[-1] == "femalechest":
        del l[-1]
        theGrid.pack_forget()
    elif button_id == 7 and l[-1] == "maleintimate":
        del l[-1]
        theGrid.pack_forget()
    elif button_id == 7 and l[-1] == "femaleintimate":
        del l[-1]
        theGrid.pack_forget()

        

def createButtons(s, theGrid):
    if s is "sex":
        
        b1 = Button(theGrid, text="Male",padx=20,pady=20, fg="black", command=lambda: OnButtonClick(theGrid,1))
        b1.pack(side=LEFT)
        b2 = Button(theGrid, text="Female",padx=20,pady=20, fg="black", command=lambda: OnButtonClick(theGrid,2))
        b2.pack(side=LEFT)
        
    elif s is "malefemale":
        b1 = Button(theGrid, text="Head",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,1)).grid(row=0,column=0)
        b1.pack(side=LEFT)
        b2 = Button(theGrid, text="Chest",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,2)).grid(row=1,column=0)
        b2.pack(side=LEFT)
        b3=Button(theGrid, text="Hands",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,3)).grid(row=2,column=0)
        b3.pack(side=LEFT)
        b4=Button(theGrid, text="Legs",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,4)).grid(row=3,column=0)
        b4.pack(side=LEFT)
        b5=Button(theGrid, text="Stomach",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,5)).grid(row=4,column=0)
        b5.pack(side=LEFT)
        b6=Button(theGrid, text="Intimate zones",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,6)).grid(row=5,column=0)
        b6.pack(side=LEFT)
        b7=Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,7))
        b7.pack(side=LEFT)
    elif s is "malefemalehead":
        b1=Button(theGrid, text="Forehead",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,1)).grid(row=0,column=0) #hir
        b1.pack(side=LEFT)
        b2=Button(theGrid, text="Nose",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,2)).grid(row=1,column=0) #lor
        b2.pack(side=LEFT)
        b3=Button(theGrid, text="Ears",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,3)).grid(row=2,column=0) #lor
        b3.pack(side=LEFT)
        b4=Button(theGrid, text="Teeth",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,4)).grid(row=3,column=0) #st
        b4.pack(side=LEFT)
        b5=Button(theGrid, text="Neck",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,5)).grid(row=4,column=0) #lor
        b5.pack(side=LEFT)
        b6=Button(theGrid, text="Eyes",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,6)).grid(row=5,column=0) #ok
        b6.pack(side=LEFT)
        b7=Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,7)).grid(row=6,column=0)
        b7.pack(side=LEFT)
    elif s is "malechest":
        b1=Button(theGrid, text="Heart",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,1)).grid(row=0,column=0) #card
        b1.pack(side=LEFT)
        b2=Button(theGrid, text="Lungs",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,2)).grid(row=1,column=0) #hir
        b2.pack(side=LEFT)
        b3=Button(theGrid, text="Gullet",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,3)).grid(row=2,column=0) #hir
        b3.pack(side=LEFT)
        b4=Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,7)).grid(row=3,column=0)
        b4.pack(side=LEFT)
    elif s is "femalechest":
        b1=Button(theGrid, text="Heart",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,1)).grid(row=0,column=0) #card
        b1.pack(side=LEFT)
        b2=Button(theGrid, text="Lungs",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,2)).grid(row=1,column=0) #hir
        b2.pack(side=LEFT)
        b3=Button(theGrid, text="Gullet",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,3)).grid(row=2,column=0) #hir
        b3.pack(side=LEFT)
        b4=Button(theGrid, text="Breast",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,4)).grid(row=3,column=0)  #mom
        b4.pack(side=LEFT)
        b5=Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,7)).grid(row=4,column=0)
        b5.pack(side=LEFT)
    elif s is "maleintimate":
        b1=Button(theGrid, text="Penis",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,1)).grid(row=0,column=0) #ur
        b1.pack(side=LEFT)
        b2=Button(theGrid, text="Butt",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,2)).grid(row=1,column=0) #pr
        b2.pack(side=LEFT)
        b3=Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,7)).grid(row=2,column=0)
        b3.pack(side=LEFT)
    elif s is "femaleintimate":
        b1=Button(theGrid, text="Vagina",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,1)).grid(row=0,column=0) #vin
        b1.pack(side=LEFT)
        b2=Button(theGrid, text="Butt",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,2)).grid(row=1,column=0) #pr
        b2.pack(side=LEFT)
        b3=Button(theGrid, text="Back",padx=20,pady=20, fg="black",command=lambda: OnButtonClick(theGrid,7)).grid(row=2,column=0)
        b3.pack(side=LEFT)
    


root = Tk()
root.title("Hack2019")
while tg is not 1:
    f = Frame(root, height=32, width=32)
    f.pack_propagate(0)
    f.pack()
    createButtons(l[-1], f)
    root.mainloop()
root.mainloop()
