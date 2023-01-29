from tkinter import *
import tkinter.messagebox

root = Tk()

root.geometry("535x600+0+0")
root.title("Game")

root.resizable(False,False)
root.config(bg="powder Blue")

buttons=StringVar()

mainframe=Frame(root,height=450,width=600).place(x=0,y=0)

def reset():
    btn1['text'] = " "
    btn2['text'] = " "
    btn3['text'] = " "
    btn4['text'] = " "
    btn5['text'] = " "
    btn6['text'] = " "
    btn7['text'] = " "
    btn8['text'] = " "
    btn9['text'] = " "

    btn1.configure(bg='gainsboro')
    btn2.configure(bg='gainsboro')
    btn3.configure(bg='gainsboro')
    btn4.configure(bg='gainsboro')
    btn5.configure(bg='gainsboro')
    btn6.configure(bg='gainsboro')
    btn7.configure(bg='gainsboro')
    btn8.configure(bg='gainsboro')
    btn9.configure(bg='gainsboro')


i=1
def checker(buttons):
    global i
    if buttons['text']==" " and i==1:
        buttons['text']="X"
        i=i+1
        winner()
    elif buttons['text']==" " and i==2:
        buttons['text']="O"
        i=i-1
        winner()

def winner():
    if btn1['text']=="X" and btn2['text']=="X" and btn3['text']=='X':
        btn1.configure(bg='powder Blue')
        btn2.configure(bg='powder Blue')
        btn3.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is X","O is Defeated by X")
        
    elif btn1['text']=="X" and btn4['text']=="X" and btn7['text']=='X':
        btn1.configure(bg='powder Blue')
        btn4.configure(bg='powder Blue')
        btn7.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is X","O is Defeated by X")

    elif btn1['text']=="X" and btn5['text']=="X" and btn9['text']=='X':
        btn1.configure(bg='powder Blue')
        btn5.configure(bg='powder Blue')
        btn9.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is X","O is Defeated by X")

    elif btn4['text']=="X" and btn5['text']=="X" and btn6['text']=='X':
        btn4.configure(bg='powder Blue')
        btn5.configure(bg='powder Blue')
        btn6.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is X","O is Defeated by X")
    elif btn7['text']=="X" and btn8['text']=="X" and btn9['text']=='X':
        btn7.configure(bg='powder Blue')
        btn8.configure(bg='powder Blue')
        btn9.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is X","O is Defeated by X")

    elif btn3['text']=="X" and btn7['text']=="X" and btn9['text']=='X':
        btn3.configure(bg='powder Blue')
        btn7.configure(bg='powder Blue')
        btn9.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is X","O is Defeated by X")

    elif btn3['text'] =="X" and btn5['text']=="X" and btn7['text']=='X':
        btn3.configure(bg='powder Blue')
        btn5.configure(bg='powder Blue')
        btn7.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is X","O is Defeated by X")

    elif btn2['text']=="X" and btn5['text']=="X" and btn8['text']=='X':
        btn2.configure(bg='powder Blue')
        btn5.configure(bg='powder Blue')
        btn8.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is X","O is Defeated by X")

    elif btn1['text']=="O" and btn2['text']=="O" and btn3['text']=='O':
        btn1.configure(bg='powder Blue')
        btn2.configure(bg='powder Blue')
        btn3.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is O","X is Defeated by O")

    elif btn2['text'] == "O" and btn5['text'] == "O" and btn8['text'] == 'O':
        btn2.configure(bg='powder Blue')
        btn5.configure(bg='powder Blue')
        btn8.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is O", "X is Defeated by O")

    elif btn1['text'] == "O" and btn4['text'] == "O" and btn7['text'] == 'O':
        btn1.configure(bg='powder Blue')
        btn4.configure(bg='powder Blue')
        btn7.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is O", "X is Defeated by O")

    elif btn1['text'] == "O" and btn5['text'] == "O" and btn9['text'] == 'O':
        btn1.configure(bg='powder Blue')
        btn5.configure(bg='powder Blue')
        btn9.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is O", "X is Defeated by O")

    elif btn4['text'] == "O" and btn5['text'] == "O" and btn6['text'] == 'O':
        btn4.configure(bg='powder Blue')
        btn5.configure(bg='powder Blue')
        btn6.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is O", "X is Defeated by O")

    elif btn7['text'] == "O" and btn8['text'] == "O" and btn9['text'] == 'O':
        btn7.configure(bg='powder Blue')
        btn8.configure(bg='powder Blue')
        btn9.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is O", "X is Defeated by O")

    elif btn3['text'] == "O" and btn6['text'] == "O" and btn9['text'] == 'O':
        btn3.configure(bg='powder Blue')
        btn6.configure(bg='powder Blue')
        btn9.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is O", "X is Defeated by O")

    elif btn3['text'] == "O" and btn5['text'] == "O" and btn7['text'] == 'O':
        btn3.configure(bg='powder Blue')
        btn5.configure(bg='powder Blue')
        btn7.configure(bg='powder Blue')
        tkinter.messagebox.showinfo("winner is O" , "X is Defeated by O")


btn1=Button(mainframe,text="",font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(btn1))
btn1.grid(row=1,column=0,sticky=S+N+E+W)

btn2=Button(mainframe,text="",font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(btn2))
btn2.grid(row=1,column=1,sticky=S+N+E+W)

btn3=Button(mainframe,text="",font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(btn3))
btn3.grid(row=1,column=2,sticky=S+N+E+W)

btn4=Button(mainframe,text="",font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(btn4))
btn4.grid(row=2,column=0,sticky=S+N+E+W)

btn5=Button(mainframe,text="",font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(btn5))
btn5.grid(row=2,column=1,sticky=S+N+E+W)

btn6=Button(mainframe,text="",font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(btn6))
btn6.grid(row=2,column=2,sticky=S+N+E+W)

btn7=Button(mainframe,text="",font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(btn7))
btn7.grid(row=3,column=0,sticky=S+N+E+W)

btn8=Button(mainframe,text="",font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(btn8))
btn8.grid(row=3,column=1,sticky=S+N+E+W)

btn9=Button(mainframe,text="",font=('times',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda :checker(btn9))
btn9.grid(row=3,column=2,sticky=S+N+E+W)

btn_reset=Button(root,text='RESET',font=('arial',15,'bold'),height=2,width=20,bg='gainsboro',padx=5,pady=10,command=reset)
btn_reset.place(x=120,y=500)

root.mainloop()