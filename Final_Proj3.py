#setup
from tkinter import *
from tkinter import messagebox
import tkinter
import random
import webbrowser

#creates window
root= tkinter.Tk()

#Labels window
root.title("Start Screen")

#sets size of window
root.geometry("1400x700")

#Create Title
Title= tkinter.Label(root, text= "Puzzle Game", font = ('Helvetica', 120))
Title.pack()

#create name entry Label
Enter_name = tkinter.Label(root, text = "Enter name below", font = ('Helvetica', 20))
Enter_name.pack()

#Create Name entry box
Name_entry = tkinter.Entry(root, bd =5)
Name_entry.pack()

# defines Enter_name function
def Enter_name():
    Name = Name_entry.get()
    print(Name)

#Create Enter button
Enter_Button = tkinter.Button(root, text = "Enter", font = ('Helvetica, 20'), command = Enter_name)
Enter_Button.pack()

#defines manual button function that runs when manual button is pressed (taken from huxley)
def Manual():
    webbrowser.open('https://docs.google.com/document/d/1sfQ2bns80TfQRgGEr5L4CWokJ0P-tr3OSZ0IhDRCFUk/edit')

#Creates game manual Button
Manual_Button = tkinter.Button(root, text = "Puzzle Manual", fg = ('Red'), font = ('Helvetica', 80), command = Manual)
Manual_Button.pack(side='bottom')

#defines start game function that runs when start button is clicked
def Start_game():
    Game= tkinter.Tk()
    Game.title("Puzzle Game")
    Game.geometry("1400x700")

    #creates instruction
    Game_title = tkinter.Label(Game, text = "Finish the puzzle as fast as possible", font = ('Helvetica', 85))
    Game_title.pack()

    #creates time left function
    
    #creates time left label
    time_left = 30
    time_title = tkinter.Label(Game, text = 'Time left :' + Str(timeleft), font= ('Helvetica', 20))
    time_title.pack()


#Creates Start Button
Start_Button = tkinter.Button(root, text = "Start", fg = ('Green'), font = ('Helvetica', 180), command = Start_game)
Start_Button.pack(side='bottom')






#Run the GUI
root.mainloop()
Game.mainloop()
