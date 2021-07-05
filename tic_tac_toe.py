from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')
root.configure(background='#E6E6FA')

label1 = Label(root, text="Player 1 : X", font="Helvetica 15",bg='#E6E6FA',)
label1.grid(row=1, column=1)

label2 = Label(root, text="Player 2 : O", font="Helvetica 15", bg='#E6E6FA')
label2.grid(row=2, column=1)


def disable_all_btns():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)

def check_if_won():
    global winner
    winner = False

    if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X":
        btn1.config(bg="red")
        btn2.config(bg="red")
        btn3.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 1 wins !!")
        disable_all_btns()
    elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
        btn4.config(bg="red")
        btn5.config(bg="red")
        btn6.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 1 wins !!")
        disable_all_btns()
    elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X":
        btn7.config(bg="red")
        btn8.config(bg="red")
        btn9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 1 wins !!")
        disable_all_btns()
    elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X":
        btn1.config(bg="red")
        btn4.config(bg="red")
        btn7.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 1 wins !!")
        disable_all_btns()
    elif btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X":
        btn2.config(bg="red")
        btn5.config(bg="red")
        btn8.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 1 wins !!")
        disable_all_btns()
    elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X":
        btn3.config(bg="red")
        btn6.config(bg="red")
        btn9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 1 wins !!")
        disable_all_btns()
    elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X":
        btn1.config(bg="red")
        btn5.config(bg="red")
        btn9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 1 wins !!")
        disable_all_btns()
    elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X":
        btn3.config(bg="red")
        btn5.config(bg="red")
        btn7.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 1 wins !!")
        disable_all_btns()
    elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O":
        btn1.config(bg="red")
        btn2.config(bg="red")
        btn3.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 2 wins!!")
        disable_all_btns()
    elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
        btn4.config(bg="red")
        btn5.config(bg="red")
        btn6.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 2 wins!!")
        disable_all_btns()
    elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O":
        btn7.config(bg="red")
        btn8.config(bg="red")
        btn9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 2 wins!!")
        disable_all_btns()
    elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O":
        btn1.config(bg="red")
        btn4.config(bg="red")
        btn7.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 2 wins!!")
        disable_all_btns()
    elif btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O":
        btn2.config(bg="red")
        btn5.config(bg="red")
        btn8.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 2 wins!!")
        disable_all_btns()
    elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O":
        btn3.config(bg="red")
        btn6.config(bg="red")
        btn9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 2 wins!!")
        disable_all_btns()
    elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O":
        btn1.config(bg="red")
        btn5.config(bg="red")
        btn9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 2 wins!!")
        disable_all_btns()
    elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O":
        btn3.config(bg="red")
        btn5.config(bg="red")
        btn7.config(bg="red")
        messagebox.showinfo("Tic Tac Toe", "Congratulations! Player 2 wins!!")
        disable_all_btns()
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "Game ties \n****No one wins****")


def btn_click(btn):
    global click, count
    if btn["text"] == " " and click == True:
        btn["text"] = "X"
        click = False
        count += 1
        check_if_won()
    elif btn["text"] == " " and click == False:
        btn["text"] = "O"
        click = True
        count += 1
        check_if_won()
    else:
        messagebox.showerror("Tic Tac Toe","Opps! Box is already selected.\n Please select remaining one.")

def reset():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global click, count
    click=True
    count = 0

    btn1 = Button(root, text=" ", width=20, height=10, bg='#E6E6FA', command=lambda: btn_click(btn1))
    btn1.grid(row=3, column=1)

    btn2 = Button(root, text=" ", width=20, height=10, bg='#E6E6FA', command=lambda: btn_click(btn2))
    btn2.grid(row=3, column=2)

    btn3 = Button(root, text=" ", width=20, height=10, bg='#E6E6FA', command=lambda: btn_click(btn3))
    btn3.grid(row=3, column=3)

    btn4 = Button(root, text=" ", width=20, height=10, bg='#E6E6FA', command=lambda: btn_click(btn4))
    btn4.grid(row=4, column=1)

    btn5 = Button(root, text=" ", width=20, height=10, bg='#E6E6FA', command=lambda: btn_click(btn5))
    btn5.grid(row=4, column=2)

    btn6 = Button(root, text=" ", width=20, height=10, bg='#E6E6FA', command=lambda: btn_click(btn6))
    btn6.grid(row=4, column=3)

    btn7 = Button(root, text=" ", width=20, height=10, bg='#E6E6FA', command=lambda: btn_click(btn7))
    btn7.grid(row=5, column=1)

    btn8 = Button(root, text=" ", width=20,height=10, bg='#E6E6FA', command=lambda: btn_click(btn8))
    btn8.grid(row=5, column=2)

    btn9 = Button(root, text=" ", width=20, height=10, bg='#E6E6FA', command=lambda: btn_click(btn9))
    btn9.grid(row=5, column=3)

start_menu = Menu(root)
root.config(menu=start_menu)

options_menu = Menu(start_menu, tearoff=False)
start_menu.add_cascade(label="OPTIONS", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)

reset()

root.mainloop()