#setup
from tkinter import *
from tkinter import messagebox
import tkinter
import random
import webbrowser

#creates dictionary for global variables
dict = {
    "wordsleft" = 10
    "strikes" = 0
    "wordcolor" = None
    "Game_word"= None
    "Name" = None
    "on_number" = 0
    "reverse_game_number" = None
    "number_label" = None
}




#creates window
root= tkinter.Tk()

#Labels window
root.title("Start Screen")

#sets size of window
root.geometry("1400x700")

#Create Title
Title= tkinter.Label(root, text= "Puzzle Game", font = ('Helvetica', 120))
Title.pack()

#Create Note
manual_note = tkinter.Label(root, text= "Click Manual Button for information about the games", fg = "blue", font = ('Helvetica', 20))
manual_note.pack()

#create name entry Label
Enter_name = tkinter.Label(root, text = "Enter name below", font = ('Helvetica', 20))
Enter_name.pack()

#Create Name entry box
Name_entry = tkinter.Entry(root, bd =5)
Name_entry.pack()

# defines Enter_name function
def Enter_name():
    global dict
    dict['Name'] = Name_entry.get()

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
    #imports global variables
    global dict

    #Window Setup
    Game= tkinter.Tk()
    Game.title("Puzzle Game")
    Game.geometry("1400x700")

    #creates instruction
    Game_title = tkinter.Label(Game, text = str(dict['Name']) + ", Finish the puzzle as fast as possible", font = ('Helvetica', 50))
    Game_title.pack()

    # defines the first Game function
    def colorgame():
        #creates the list of colors
        color_values = ['Blue', 'Yellow', 'Green', 'Black', 'Red', 'Purple', 'Orange']

        #creates the entry box
        Game_entry= tkinter.Entry(Game, bd=10, font = ('Helvetica', 75))
        Game_entry.pack(side = 'bottom')
        Game_entry.focus()

        #defines the word maker
        def word_maker():
            import dict

            #selects words from list
            word = random.choice(color_values)
            dict['wordcolor']= random.choice(color_values)

            #creates word label
            dict['Game_word'] = tkinter.Label(Game, text = word, fg = dict['wordcolor'], font = ('Helvetica', 200))
            dict['Game_word'].pack(side = 'bottom')


        #creates strike indication widget
        Strike_X = tkinter.Label(Game, text = 'X', fg = 'Red', font = ('Helvetica', 200))
        Strike_XX = tkinter.Label(Game, text = 'XX', fg = 'Red', font = ('Helvetica', 200))

        #defines check entry function

        def check_entry(arg):
            global dict
            color_game_entry = Game_entry.get()
            if dict['wordcolor'] == str(color_game_entry):
                dict['wordsleft']-=1
                dict['Game_word'].pack_forget()
                word_maker()
                if dict['wordsleft'] == 0:
                    You_Win = tkinter.Tk()
                    You_Win.title("You Win!")
                    You_Win.geometry("1400x700")
                    Congratulations= tkinter.Label(You_Win, text = "Congratulations " + Name + ", You Won!", font = ('Helvetica', 100))
                    Congratulations.pack()
            else:
                dict['strikes'] += 1
                if dict['strikes'] == 1:
                    Strike_X.pack(side='left')
                if dict['strikes'] == 2:
                    Strike_X.pack_forget()
                    Strike_XX.pack(side= 'left')
                if dict['strikes'] == 3:
                    webbrowser.open('https://www.youtube.com/watch?v=NIPNf6HVefM')

        #binds the check_entry functoin to return
        Game.bind('<Return>', check_entry)
        word_maker()

    def numbergame():

        #makes entry box
        number_game_entry= tkinter.Entry(Game, bd=10, font = ('Helvetica', 75))
        number_game_entry.pack(side = 'bottom')
        number_game_entry.focus()

        #defines number reverse function(from Sanfoundry)
        def number_reverse(number):
            n = number
            rev=0
            while(n>0):
                dig=n%10
                rev=rev*10+dig
                n=n//10
            return rev

        #creates strike indication widget
        Strike_X = tkinter.Label(Game, text = 'X', fg = 'Red', font = ('Helvetica', 200))
        Strike_XX = tkinter.Label(Game, text = 'XX', fg = 'Red', font = ('Helvetica', 200))


        def create_nums():
            global reverse_game_number
            global number_label
            #defines number
            gamenumber = random.randint(100000,999999)
            # reverse_game_number =
            reverse_game_number = number_reverse(gamenumber)

            #makes number label
            number_label = tkinter.Label(Game, text = str(gamenumber), font= ('Helvetica', 200))
            number_label.pack(side= 'bottom')

        #runs create_nums
        create_nums()

        #defines check number function
        def check_number():
            global strikes
            global reverse_game_number
            global number_label
            global on_number
            global Name
            number_answer = number_game_entry.get()
            if str(reverse_game_number) == number_answer:
                number_label.pack_forget()
                on_number+= 1
                if on_number >2:
                    You_Win = tkinter.Tk()
                    You_Win.title("You Win!")
                    You_Win.geometry("1400x700")
                    Congratulations= tkinter.Label(You_Win, text = "Congratulations " + Name + ", You Won!", font = ('Helvetica', 100))
                    Congratulations.pack()
                else:
                    create_nums()
            else:
                strikes += 1
                if strikes == 1:
                    Strike_X.pack(side='left')
                if strikes == 2:
                    Strike_X.pack_forget()
                    Strike_XX.pack(side= 'left')
                if strikes == 3:
                    webbrowser.open('https://www.youtube.com/watch?v=NIPNf6HVefM')

        #makes check button
        number_check_button= tkinter.Button(Game, text= 'Check', font= ('Helvetica', 50), command= check_number)
        number_check_button.pack(side= 'right')

    rand = random.randint(1,2)
    if rand == 1:
        numbergame()
    if rand == 2:
        colorgame()

    #creates timeleft var
    timeleft= 30
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
    countdown(30)

    Game.mainloop()



#Creates Start Button
Start_Button = tkinter.Button(root, text = "Start", fg = ('Green'), font = ('Helvetica', 180), command = Start_game)
Start_Button.pack(side='bottom')






#Run the GUI
root.mainloop()
