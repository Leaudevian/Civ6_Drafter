import random as rd
from tkinter import *

liste_civ = ["American","Arabian","Aztec","Brazilian","Chinese","Egyptian","English","French","German","Greek","Indian","Japanese","Kongolese","Norwegian","Roman","Russian","Scythian","Spanish","Sumerian"]
ban=[]

mainpage = Tk()
mainpage.title("Civ6_Drafter")
mainpage.geometry("720x480")
mainpage.minsize(600, 360)
mainpage.iconbitmap("icon.ico")
mainpage.config(background='#687bd3')

framestart = Frame(mainpage, bg='#687bd3')

label_title = Label(framestart, text="Civ6_Drafter", font=("Courrier", 40), bg='#687bd3', fg='white')
label_title.pack()

label_subtitle = Label(framestart, text="Civilization drafter for Civ6 base game", font=("Courrier", 25), bg='#687bd3', fg='white')
label_subtitle.pack()

framestart.pack(expand=YES)

def addban1(buttonframe):
    ban.append("American")

def addban2():
    ban.append("Arabian")

def addban3():
    ban.append("Aztec")

def addban4():
    ban.append("Brazilian")

def addban5():
    ban.append("Chinese")

def addban6():
    ban.append("Egyptian")

def addban7():
    ban.append("English")

def addban8():
    ban.append("French")

def addban9():
    ban.append("German")

def addban10():
    ban.append("Greek")

def addban11():
    ban.append("Indian")

def addban12():
    ban.append("Japanese")

def addban13():
    ban.append("Kongolese")

def addban14():
    ban.append("Norwegian")

def addban15():
    ban.append("Roman")

def addban16():
    ban.append("Russian")

def addban17():
    ban.append("Scythian")

def addban18():
    ban.append("Spanish")

def addban19():
    ban.append("Sumerian")

def civban():
    framestart.destroy()

    banframe = Frame(mainpage, bg='#687bd3')
    label_title = Label(banframe, text="Choose 5 banned Civilization", font=("Courrier", 40), bg='#687bd3', fg='white')
    label_title.pack()

    label_subtitle = Label(banframe, text="Civilization drafter for Civ6 base game", font=("Courrier", 25), bg='#687bd3', fg='white')
    label_subtitle.pack()
    
    banframe.pack(expand=YES)

    buttonframe = Frame(mainpage, bg='#687bd3')

    button1=Button(buttonframe,text="American", command=addban1)
    button1.grid(row=0,column=0)

    button2=Button(buttonframe, text="Arabian", command=addban2)
    button2.grid(row=0,column=1)

    button3=Button(buttonframe,text=" Aztec ", command=addban3)
    button3.grid(row=0,column=2)

    button4=Button(buttonframe,text="Brazillian", command=addban4)
    button4.grid(row=0,column=3)

    button5=Button(buttonframe,text="Chinese", command=addban5)
    button5.grid(row=0,column=4)

    button6=Button(buttonframe,text="Egyptian", command=addban6)
    button6.grid(row=0,column=5)

    button7=Button(buttonframe,text="English", command=addban7)
    button7.grid(row=0,column=6)

    button8=Button(buttonframe,text=" French", command=addban8)
    button8.grid(row=0,column=7)

    button9=Button(buttonframe,text="German", command=addban9)
    button9.grid(row=0,column=8)

    button10=Button(buttonframe,text=" Greek ", command=addban10)
    button10.grid(row=1,column=0)

    button11=Button(buttonframe,text="Indian", command=addban11)
    button11.grid(row=1,column=1)

    button12=Button(buttonframe,text="Japanese", command=addban12)
    button12.grid(row=1,column=2)

    button13=Button(buttonframe,text="Kongolese", command=addban13)
    button13.grid(row=1,column=3)

    button14=Button(buttonframe,text="Norvegian", command=addban14)
    button14.grid(row=1,column=4)

    button15=Button(buttonframe,text=" Roman ", command=addban15)
    button15.grid(row=1,column=5)

    button16=Button(buttonframe,text="Russian", command=addban16)
    button16.grid(row=1,column=6)

    button17=Button(buttonframe,text="Scythian", command=addban17)
    button17.grid(row=1,column=7)

    button18=Button(buttonframe,text="Spanish", command=addban18)
    button18.grid(row=1,column=8)

    button19=Button(buttonframe,text="Sumerian", command=addban19)
    button19.grid(row=2,column=0)

    buttonframe.pack(expand=YES)

    def finaldraft():
        banframe.destroy()
        buttonframe.destroy()
        finalframe.destroy()

        for i in ban:
            liste_civ.remove(i)

        equipe1,equipe2=[],[]

        for i in range(0,7):
            value=rd.randint(0,len(liste_civ)-1)
            equipe1.append(liste_civ[value])
            liste_civ.remove(liste_civ[value])

        equipe1frame = Frame(mainpage, bg='#687bd3')

        labelequipe1 = Label(equipe1frame, text="Equipe 1:", font=("Courrier", 25), bg='#687bd3', fg='white')
        labelequipe1.pack(side=TOP, expand=YES)

        team1 = Listbox(equipe1frame)
        team1.pack(expand=YES)

        for item in equipe1:
            team1.insert(END, item)

        equipe1frame.pack(expand=YES, side=LEFT)

        equipe2frame = Frame(mainpage, bg='#687bd3')

        labelequipe2 = Label(equipe2frame, text="Equipe 2:", font=("Courrier", 25), bg='#687bd3', fg='white')
        labelequipe2.pack(side=TOP, expand=YES)

        team2 = Listbox(equipe2frame)
        team2.pack(expand=YES)

        for item in liste_civ:
            team2.insert(END, item)

        equipe2frame.pack(expand=YES, side=RIGHT)


        
    finalframe = Frame(mainpage, bg='#687bd3')

    endban = Button(finalframe,text="Done !", command=finaldraft)
    endban.pack(pady=25, fill=X)

    finalframe.pack(expand=YES)





begin_button = Button(framestart, text="begin", font=("Courrier", 25), bg='white', fg='#687bd3', command=civban)
begin_button.pack(pady=25, fill=X)


mainpage.mainloop()