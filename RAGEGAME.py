# You try to click a circle, but when you hover over it, it dissapears

# Things to do:
# 1. Make Game (DONE) (thanks, stackoverflow!)
# 1.5. Make modes (Easy, Normal, Hard, MADE IMPOSSIBLE) (DONE) (thanks, stackoverflow!) x2
# BTW made score
# 2. Make title screen (uhh..)
# 3. Make shop system
# 4. Make it an .exe file
# 5. Make a YouTube video about it.

import threading
import time
from tkinter import *
import random

x = 0

str_i= ""

def game():

    gui = Tk()

    gui.after(1, lambda: gui.focus_force())

    gui.configure(bg="limegreen")

    gui.title("                                                                                                                                                                                                   Game")

    gui.geometry("1280x800")

    gui.resizable(False, False)

    my_label=Label(gui, text="",font='helvetica,12', bg='limegreen', fg='white')
    my_label.pack(pady=50)  

    but_loc_x=[200,600,1000]
    but_loc_y=[200,350,600]
    zbut_loc_x=[200,600,1000]
    zbut_loc_y=[200,350,600]
    obut_loc_x=[200,600,1000]
    obut_loc_y=[200,350,600]

    def press():
        my_label.config(text="You pressed me.\n Well done\n")   
        rage_button3.place_forget()
        rage_button2.place_forget()
        imp_rage_button.place_forget()
        rage_button.place_forget()
        global x
        global str_i
        x=x+1
        str_i = str(x)
        label=Label(gui, text="Score-"+str_i,font='helvetica,12', bg='limegreen', fg='white')
        label.place(x=1160,y=10)

    def button_hover_hard(z):
        gui.after(75)
        obut_pos_x=random.choice(obut_loc_x)   
        obut_pos_y=random.choice(obut_loc_y) 
        rage_button2.place_configure(x=obut_pos_x,y=obut_pos_y)

    def button_hover_easy(x):
        gui.after(175)
        zbut_pos_x=random.choice(zbut_loc_x)
        zbut_pos_y=random.choice(zbut_loc_y) 

        rage_button3.place_configure(x=zbut_pos_x,y=zbut_pos_y)  

    def button_hover(e):
        gui.after(125)
        but_pos_x=random.choice(but_loc_x)   
        but_pos_y=random.choice(but_loc_y)   
        rage_button.place_configure(x=but_pos_x,y=but_pos_y)

    def impbutton_hover(e):
        gui.after(25)
        impbut_pos_x=random.choice(but_loc_x)   
        impbut_pos_y=random.choice(but_loc_y)   
        imp_rage_button.place_configure(x=impbut_pos_x,y=impbut_pos_y)

    def easy1():
        rage_button2.place_forget()
        rage_button.place_forget()
        imp_rage_button.place_forget()
        rage_button3.place(x=600,y=350,anchor=CENTER)

    def normal1():
        rage_button3.place_forget()
        rage_button2.place_forget()
        imp_rage_button.place_forget()
        rage_button.place(x=600,y=350,anchor=CENTER)

    def hard1():
        rage_button3.place_forget()
        rage_button.place_forget()
        imp_rage_button.place_forget()
        rage_button2.place(x=600,y=350,anchor=CENTER)

    def imp1():
        rage_button.place_forget()
        rage_button3.place_forget()
        rage_button2.place_forget()
        imp_rage_button.place(x=600,y=350,anchor=CENTER)

    def CREDIT():
        gui = Tk()

        gui.configure(bg='limegreen')

        gui.title("About")

        gui.geometry("300x100")

        gui.resizable(False, False)

        L =	Label(gui, text="Made by Manik Sharma (THEOP05). \n All rights reserved.", font='helvetica,24', fg='white', bg='green')
        L.place(x=20,y=30)

    easy = Button(gui, text=' EASY ', font='helvetica,24', command=easy1)
    easy.place(x=10,y=10)
    normal = Button(gui, text=' NORMAL ', font='helvetica,24',  command=normal1)
    normal.place(x=10, y=50)
    hard = Button(gui, text=' HARD ', font='helvetica,24',  command=hard1)
    hard.place(x=10,y=90)
    imp = Button(gui, text=' IMPOSSIBLE ', font='helvetica,24',  command=imp1)
    imp.place(x=10,y=130)

    rage_button =Button(gui,text=" Try to \n click me \n >:) ",borderwidth=0,command=press,height=3, width=5 )

    rage_button.bind("<Enter>",button_hover)

    rage_button2 =Button(gui,text=" Try to \n click me \n >:) ",borderwidth=0,command=press,height=3, width=5 )

    rage_button2.bind("<Enter>",button_hover_hard)

    rage_button3 =Button(gui,text=" Try to \n click me \n >:) ",borderwidth=0,command=press,height=3, width=5 )

    rage_button3.bind("<Enter>",button_hover_easy)

    imp_rage_button =Button(gui,text=" Try to \n click me \n >:) ",borderwidth=0,command=press,height=3, width=5 )

    imp_rage_button.bind("<Enter>",impbutton_hover)

    CREDITS = Button(gui, text="ABOUT", font='helvetica,24', command=CREDIT)
    CREDITS.place(x=10,y=760)

def titlescreen():
    
    def CREDIT():
        gi = Tk()

        gi.configure(bg='limegreen')

        gi.title("About")

        gi.geometry("300x100")

        gi.resizable(False, False)

        L =	Label(gi, text="Made by Manik Sharma (THEOP05). \n All rights reserved.", font='helvetica,24', fg='white', bg='green')
        L.place(x=20,y=30)

    gi = Tk()

    gi.configure(bg="limegreen")

    gi.after(1, lambda: gi.focus_force())

    gi.title("Game Splash Screen")

    gi.resizable(False, False)

    L = Label(gi, text="Game",font='helvetica,24', bg='green', fg='white' )
    L.pack(pady=50)

    def pla1():
        gi.after(5, gi.destroy)

    gi.geometry("480x240")

    play = Button(gi, text='PLAY!', font='helvetica,36', command=lambda: [game(), pla1()])
    play.place(x=210, y=120)

    pla = Button(gi, text='QUIT', font='helvetica,36', command=pla1)
    pla.place(x=215, y=170)

    CREDITS = Button(gi, text="ABOUT", font='helvetica,24', command=CREDIT)
    CREDITS.place(x=400,y=200)



titlescreen()

gu = Tk()
gu.after(1,gu.destroy)

#button.bind("<Leave>",unhover)

gu.mainloop()