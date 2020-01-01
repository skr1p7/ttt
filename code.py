#!usr/bin/python3

from tkinter import *
import tkinter.messagebox
import os

def main():
    global bclick, flag, p1Name, p2Name, p2win, p1win
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global p1, p2, tk
    tk = Tk()
    tk.title("Cross n Nots")
    tk.resizable(False, False)
    p1win = StringVar()
    p2win = StringVar()
    p1 = StringVar()
    p2 = StringVar()
    p1Name = Entry(tk, textvariable=p1, bd=5)
    p1Name.grid(row=1, column=1, columnspan=8)
    p2Name = Entry(tk, textvariable=p2, bd=5)
    p2Name.grid(row=2, column=1, columnspan=8)
    bclick = True
    flag = 0



    buttons = StringVar()
    label = Label( tk, text="Player 1:", font='ComicSans', bg='white', fg='black', height=1, width=8)
    label.grid(row=1, column=0)
    label = Label( tk, text="Player 2:", font='ComicSans', bg='white', fg='black', height=1, width=8)
    label.grid(row=2, column=0)
    button1 = Button(tk, text=" ", font='ComicSans', bg='lightblue', fg='black', height=4, width=8, command=lambda: click(button1))
    button1.grid(row=3, column=0)
    button2 = Button(tk, text=' ', font='ComicSans', bg='lightblue', fg='black', height=4, width=8, command=lambda: click(button2))
    button2.grid(row=3, column=1)
    button3 = Button(tk, text=' ',font='ComicSans', bg='lightblue', fg='black', height=4, width=8, command=lambda: click(button3))
    button3.grid(row=3, column=2)
    button4 = Button(tk, text=' ', font='ComicSans', bg='lightblue', fg='black', height=4, width=8, command=lambda: click(button4))
    button4.grid(row=4, column=0)
    button5 = Button(tk, text=' ', font='ComicSans', bg='lightblue', fg='black', height=4, width=8, command=lambda: click(button5))
    button5.grid(row=4, column=1)
    button6 = Button(tk, text=' ', font='ComicSans', bg='lightblue', fg='black', height=4, width=8, command=lambda: click(button6))
    button6.grid(row=4, column=2)
    button7 = Button(tk, text=' ', font='ComicSans', bg='lightblue', fg='black', height=4, width=8, command=lambda: click(button7))
    button7.grid(row=5, column=0)
    button8 = Button(tk, text=' ', font='ComicSans', bg='lightblue', fg='black', height=4, width=8, command=lambda: click(button8))
    button8.grid(row=5, column=1)
    button9 = Button(tk, text=' ', font='ComicSans', bg='lightblue', fg='black', height=4, width=8, command=lambda: click(button9))
    button9.grid(row=5, column=2)
    tk.mainloop()

def reset():
    if tkinter.messagebox.askyesno("Cross n Nots", "Do You wanna play the game again?") == True:
        tk.destroy()
        main()
    else:
        exit()

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def click(buttons):
    if not p1.get() and not p2.get():
        tkinter.messagebox.showinfo("Cross n Nots", "Please Enter The Players Name: ")
    else:
        global bclick, flag, p1Name, p2Name, p2win, p1win
        if buttons["text"] == " " and bclick == True:
            buttons["text"] = "X"
            bclick = False
            p2win = p2.get() + " won"
            p1win = p1.get() + " won"
            winner()
            flag += 1
        elif buttons["text"] == " " and bclick == False:
            buttons["text"] = "O"
            bclick = True
            winner()
            flag += 1
        else:
            tkinter.messagebox.showinfo("Warning", "Choose other box!")

def winner():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Cross n Nots", p1win)
        reset()
    elif(flag == 8):
        tkinter.messagebox.showinfo("Cross n Nots", "The game is a tie.")
        reset()
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Cross n Nots", p2win)
        reset()

if __name__ == "__main__":
    main()