from tkinter import *
from PIL import Image, ImageTk
from random import randint
window=Tk()
window.title("Rock Paper Scissor")
window.configure(background="lightblue")
image_rock1=ImageTk.PhotoImage(Image.open("C:/Users/DELL/OneDrive/Desktop/r2.jpg"))
image_paper1=ImageTk.PhotoImage(Image.open("C:/Users/DELL/OneDrive/Desktop/p2.jpg"))
image_scissor1=ImageTk.PhotoImage(Image.open("C:/Users/DELL/OneDrive/Desktop/s2.jpg"))
image_rock2=ImageTk.PhotoImage(Image.open("C:/Users/DELL/OneDrive/Desktop/r1.jpg"))
image_paper2=ImageTk.PhotoImage(Image.open("C:/Users/DELL/OneDrive/Desktop/p1.jpg"))
image_scissor2=ImageTk.PhotoImage(Image.open("C:/Users/DELL/OneDrive/Desktop/s1.jpg"))


label_player=Label(window,image=image_scissor1)
label_computer=Label(window,image=image_scissor2)
label_computer.grid(row=1,column=0)
label_player.grid(row=1,column=4)

computer_score=Label(window,text=0,font=('arial',60,"bold"),fg="red")
player_score=Label(window,text=0,font=('arial',60,"bold"),fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)
player_indicator=Label(window,font=("Brush script MT",40,"bold"),text="PLAYER",bg="#8114B8",fg="#c99e9c")
computer_indicator=Label(window,font=("Brush script MT",40,"bold"),text="Computer",bg="#8114B8",fg="#c99e9c")
computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0,column=3)

def msg_updation(a):
    final_message['text']=a

def Computer_update():
    final=int(computer_score['text'])
    final+=1
    computer_score["text"]=str(final)
def player_update():
    final=int(player_score['text'])
    final+=1
    player_score["text"]=str(final)
def winner_check(p,c):
    if p==c:
        msg_updation("TIE")
    elif p=="rock":
        if c=="paper":
            msg_updation("computer wins")
            Computer_update()
        else:
            msg_updation("player wins")
            player_update()
    elif p=="paper":
        if c=="scissor":
            msg_updation("computer wins")
            Computer_update()
        else:
            msg_updation("player wins")
            player_update()
    elif p=="scissor":
        if c=="rock":
            msg_updation("computer wins")
            Computer_update()
        else:
            msg_updation("player wins")
            player_update()
    else:
        pass

to_select=["rock","paper","scissor"]
def choice_update(a):
    choice_computer=to_select[randint(0,2)]
    if choice_computer=="rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer=="paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)
    if a=="rock":
        label_player.configure(image=image_rock1)
    elif a=="paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)

    winner_check(a,choice_computer)





final_message=Label(window,font=("courier new",40,"bold"),bg="green",fg="white")
final_message.grid(row=3,column=2)

button_rock=Button(window,width=16,height=3,text="ROCK",font=("",20,"bold"),bg="#fcbcd5",fg="green",command=lambda:choice_update("rock")).grid(row=2,column=1)
button_paper=Button(window,width=16,height=3,text="PAPER",font=("arial",20,"bold"),bg="#fcbcd5",fg="green",command=lambda:choice_update("paper")).grid(row=2,column=2)
button_scissor=Button(window,width=16,height=3,text="SCISSOR",font=("arial",20,"bold"),bg="#fcbcd5",fg="green",command=lambda:choice_update("scissor")).grid(row=2,column=3)
window.mainloop()
