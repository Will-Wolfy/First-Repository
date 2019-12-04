#setup
from tkinter import *
from tkinter import messagebox
import tkinter
import random
import webbrowser

#Sets words left and strike variable
wordsleft = 10
strikes = 0

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

    # defines the first Game function
    def colorgame():
        #creates the list of colors
        color_values = ['Blue', 'Yellow', 'Green', 'Black', 'Red', 'Purple', 'Orange']

        #creates the entry box
        Game_entry= tkinter.Entry(Game, bd=50, font = ('Helvetica', 50))
        Game_entry.pack(side = 'bottom')

        #defines the word maker
        def word_maker():
            #selects words from list
            word = random.choice(color_values)
            wordcolor= random.choice(color_values)

            #creates word label
            Game_word = tkinter.Label(Game, text = word, fg = wordcolor, font = ('Helvetica', 200))
            Game_word.pack(side = 'bottom')

        #creates strike indication widget
        Strike_X = tkinter.Label(Game, text = 'X', fg = 'Red', font = ('Helvetica', 50))

        #defines check entry function

        def check_entry(arg):
            global wordsleft
            global strikes
            color_game_entry = Game_entry.get()
            wordsleft-=1
            if wordcolor == str(color_game_entry):
                word_maker()
                if wordsleft == 0:
                    You_Win= tkinter.Tk()
                    You_Win.title("You Win!")
                    You_Win.geometry("1400x700")
                    Congrats = tkinter.Label(You_Win, text= 'Congratulations, You Win!', font = ('Helvetica'))
            else:
                Strike_X.pack(side='left')
                strikes += 1
                if strike == 3:
                    webbrowser.open('https://www.youtube.com/watch?v=NIPNf6HVefM')

        #binds the check_entry functoin to return
        Game.bind('<Return>', check_entry)
        word_maker()

    colorgame()

    #creates timeleft var
    timeleft= 60
    #creates time left label
    time_title = tkinter.Label(Game, text = 'Time left : ' + str(timeleft) + ' seconds', font= ('Helvetica', 50))
    time_title.pack()
    #defines the again function
    def again(timeleft):
        timeleft-=1
        time_title.config(text='Time left : ' + str(timeleft) + ' seconds')
        if timeleft> 1:
            countdown(timeleft)
        else:
            webbrowser.open('https://www.youtube.com/watch?v=NIPNf6HVefM')
    #defines countdown function
    def countdown(timeleft):
        time_title.after(1000,again, timeleft)

    #runs countdown
    countdown(60)

    Game.mainloop()



#Creates Start Button
Start_Button = tkinter.Button(root, text = "Start", fg = ('Green'), font = ('Helvetica', 180), command = Start_game)
Start_Button.pack(side='bottom')






#Run the GUI
root.mainloop()
