#setup
from tkinter import *
from tkinter import messagebox
import tkinter
import random
import time

#creates window
root= tkinter.Tk()

#Labels window
root.title("PUZZLE GAME")

#sets size of window
root.geometry("1600x1000")


#Create Title
Title= tkinter.Label(root, text= "Puzzle Game", font = ('Helvetica', 120))
Title.pack()

#Creates game manual Button
Manual_Button = tkinter.Button(root, text = "Manual", fg = ('Red'), font = ('Helvetica', 80))
Manual_Button.pack(side='bottom')

#Creates Start Button
Start_Button = tkinter.Button(root, text = "Start", fg = ('Green'), font = ('Helvetica', 180))
Start_Button.pack(side='bottom')


#Set Background Image (From Stack overflow user Abhijeet Sinha)
# C = Canvas(root, bg="blue", height=250, width=300)
# Background = tkinter.PhotoImage("https://images2.minutemediacdn.com/image/upload/c_crop,h_3152,w_5616,x_0,y_580/f_auto,q_auto,w_1100/v1555005360/shape/mentalfloss/502944-istock-492597439.jpg")
# background_label = tkinter.Label(root, image=Background)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
# C.pack()



#Run the GUI
root.mainloop()
