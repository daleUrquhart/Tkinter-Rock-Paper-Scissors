# TKinter Rock Paper Scissors


# VARIABLE CONTROL SETTINGS
import tkinter as tk
import random as rand
import time
from PIL import Image,ImageTk
root = tk.Tk()
score = [0, 0, 0]
result = ['You Win', 'Draw', 'You Loose']
C_Input_Text = ['I Chose Rock', 'I Chose Paper', 'I Chose Scissors']


# CANVAS CONTROL SETTINGS
countdown_colour = 'orange'
main_bg_colour = 'purple'
width1 = 800 # Window Width
height1 = 600 # Window Height
canvas = tk.Canvas(root, width=width1, height=height1, bg=main_bg_colour)
root.title(" Rock Paper Scissors App ")
frame = tk.Frame(root)
frame.pack()
canvas.pack()


def countdown_clear():
    clear = tk.Label(root, text= ('_____________'), font = ('helvetica', 30), bg=main_bg_colour, fg=main_bg_colour, width=10)
    canvas.create_window(300, 400, window=clear)

    
def countdown():
    
    time.sleep(1)
    res='' #res was undeclared, not sure what it was supposed to represent

    RES = tk.Label(root, text=("3...", res), bg=countdown_colour, font=("Comic Sans", 30))               
    canvas.create_window(300,400, window=RES)
    
    time.sleep(1)
    
    countdown_clear()
    
    RES = tk.Label(root, text=("2..", res), bg=countdown_colour, font=("Comic Sans", 30))               
    canvas.create_window(300,400, window=RES)
    
    time.sleep(1)
    
    countdown_clear()
    
    RES = tk.Label(root, text=("1.", res), bg=countdown_colour, font=("Comic Sans", 30))               
    canvas.create_window(300,400, window=RES)

    time.sleep(1)
    
    countdown_clear()

    RES = tk.Label(root, text=("GO!", res), bg=countdown_colour, font=("Comic Sans", 30))               
    canvas.create_window(300,400, window=RES)

    main()


# PICTURE CLEAR CONTROL SETTINGS
def picture_clear():
    clear1 = tk.Label(root, text= ('_____________'), font = ('helvetica', 40), bg=main_bg_colour, fg=main_bg_colour, width=25)
    canvas.create_window(300, 400, window=clear1)

def main():
    rock_button=tk.Button(text='Rock', command=rock, bg='lime', fg='black', font=('Comic Sans', 9, 'bold'),width=15)
    canvas.create_window(90, 190, window=rock_button)

    paper_button=tk.Button(text='Paper', command=paper, bg='yellow', fg='black', font=('Comic Sans', 9, 'bold'),width=15)
    canvas.create_window(90, 220, window=paper_button)

    scissors_button=tk.Button(text='Scissors', command=scissors, bg='orange', fg='black', font=('Comic Sans', 9, 'bold'),width=15)
    canvas.create_window(90, 250, window=scissors_button)
    

def rock(): # ROCK CONTROL SETTINGS
    picture_clear()    
    C_Input = rand.randint(1,3)
    
    '''
    image=Image.open('rock.jpeg')
    image.thumbnail((300,300),Image.ANTIALIAS)    
    photo=ImageTk.PhotoImage(image)    
    label_image=tk.Label(image=photo)
    label_image.column,row
    

    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    img = Image.open("<path/image_name>")
    image1 = img.resize((50, 50), Image.ANTIALIAS)
    '''

    image1 = Image.open("rock.jpeg")
    test = ImageTk.PhotoImage(image1)    
    label1 = tk.Label(image=test)
    label1.image = test
    label1.configure(background=main_bg_colour)
    label1.place(x=425, y=0)
    
    if C_Input==1:
        res=result[1]
        score[1]+=1
        C_res=C_Input_Text[0]
        
    elif C_Input==2:
        res=result[2]
        score[2]+=1
        C_res=C_Input_Text[1]
     
    elif C_Input==3:
        res=result[0]
        score[0]+=1
        C_res=C_Input_Text[2]
    
    scores()

    clear1 = tk.Label(root, text= ('_____________'), font = ('helvetica', 30), bg=main_bg_colour, fg=main_bg_colour, width=20)
    canvas.create_window(300, 400, window=clear1)
    
    RES = tk.Label(root, text=("Result: ", res), bg=main_bg_colour, font=("Comic Sans", 30))               
    canvas.create_window(300,400, window=RES)

    clear2 = tk.Label(root, text= ('_____________'), font = ('helvetica', 30), bg=main_bg_colour, fg=main_bg_colour, width=20)
    canvas.create_window(300, 500, window=clear2)
    
    C_RES = tk.Label(root, text=(C_res), bg=main_bg_colour, font=("Comic Sans", 30))               
    canvas.create_window(300,500, window=C_RES)
    



def paper(): # PAPER CONTROL SETTINGS
    picture_clear()
    C_Input = rand.randint(1,3)

    image1 = Image.open("paper.jpeg")
    test = ImageTk.PhotoImage(image1)    
    label1 = tk.Label(image=test)
    label1.image = test
    label1.configure(background='purple')
    label1.place(x=425, y=0)
    
    if C_Input==1:
        res=result[0]
        score[0]+=1
        C_res=C_Input_Text[0]
    
    elif C_Input==2:
        res=result[1]
        score[1]+=1
        C_res=C_Input_Text[1]
       
    elif C_Input==3:
        res=result[2]
        score[2]+=1
        C_res=C_Input_Text[2]
    
    scores()

    clear1 = tk.Label(root, text= ('_____________'), font = ('helvetica', 30), bg=main_bg_colour, fg=main_bg_colour, width=20)
    canvas.create_window(300, 400, window=clear1)
    
    RES = tk.Label(root, text=("Result: ", res), bg=main_bg_colour, font=("Comic Sans", 30))               
    canvas.create_window(300,400, window=RES)

    clear2 = tk.Label(root, text= ('_____________'), font = ('helvetica', 30), bg=main_bg_colour, fg=main_bg_colour, width=20)
    canvas.create_window(300, 500, window=clear2)
    
    C_RES = tk.Label(root, text=(C_res), bg=main_bg_colour, font=("Comic Sans", 30))               
    canvas.create_window(300,500, window=C_RES)
    



def scissors(): # SCISSORS CONTROL SETTINGS
    picture_clear()
    C_Input = rand.randint(1,3)
    
    image1 = Image.open("scissors.jpeg")
    test = ImageTk.PhotoImage(image1)    
    label1 = tk.Label(image=test)
    label1.image = test
    label1.configure(background='purple')
    label1.place(x=425, y=0)
    
    if C_Input==1:
        res=result[2]
        score[2]+=1
        C_res=C_Input_Text[0]
       
    elif C_Input==2:
        res=result[0]
        score[0]+=1
        C_res=C_Input_Text[1]
        
    elif C_Input==3:
        res=result[1]
        score[1]+=1
        C_res=C_Input_Text[2]
        
    scores()

    clear1 = tk.Label(root, text= ('_____________'), font = ('helvetica', 30), bg=main_bg_colour, fg=main_bg_colour, width=20)
    canvas.create_window(300, 400, window=clear1)
    
    RES = tk.Label(root, text=("Result: ", res), bg=main_bg_colour, font=("Comic Sans", 30))               
    canvas.create_window(300,400, window=RES)

    clear2 = tk.Label(root, text= ('_____________'), font = ('helvetica', 30), bg=main_bg_colour, fg=main_bg_colour, width=20)
    canvas.create_window(300, 500, window=clear2)
    
    C_RES = tk.Label(root, text=(C_res), bg=main_bg_colour, font=("Comic Sans", 30))               
    canvas.create_window(300,500, window=C_RES)




def scores(): # SCORE DISPLAY CONTROL SETTINGS
    
    wins = tk.Label(root, text=("Wins: ", score[0]), bg=main_bg_colour, font=("Comic Sans", 30))
    canvas.create_window(300,100, window=wins)
    
    draws = tk.Label(root, text=("Draws: ", score[1]), bg=main_bg_colour, font=("Comic Sans", 30))
    canvas.create_window(300,200, window=draws)
    
    losses = tk.Label(root, text=("Losses: ", score[2]), bg=main_bg_colour, font=("Comic Sans", 30))
    canvas.create_window(300,300, window=losses)

countdown()
root.mainloop()