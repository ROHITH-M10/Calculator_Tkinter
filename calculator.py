from tkinter import *
from tkinter.ttk import *

root = Tk()

root.title("Calculator")
root.configure(background="light blue")
root.resizable(False, False)

myLabel = Label(root, text="CALCULATOR", font=("Comic Sans MS", 20, "bold"),background="light blue")  
myLabel.grid(row=0, column=1, padx=10, pady=10, sticky="n")  

operation = ""

e = Entry(root, font=("Comic Sans MS", 20))
e.grid(row=1, column=0, columnspan=10, padx=20, pady=10, sticky="ew") 



def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def build_add():
    global operation
    operation = "add"
    global first
    first = float(e.get())
    e.delete(0,END)

def button_sub():
    global operation
    operation = "sub"
    global first
    first = float(e.get())
    e.delete(0,END)

def button_mul():
    global operation
    operation = "mul"
    global first
    first = float(e.get())
    e.delete(0,END)

def button_div():
    global operation
    operation = "div"
    global first
    first = float(e.get())
    e.delete(0,END)

def button_equal():
    global second
    second = float(e.get())
    e.delete(0,END)

    if operation == "add":
        e.insert(0,first+second)

    elif operation == "sub":
        e.insert(0,first-second)

    elif operation == "mul":
        e.insert(0,first*second)
    
    elif operation == "div":
        e.insert(0,first/second)

def button_clear():
    global first
    first = 0
    global second
    second = 0
    e.delete(0,END)

 
# Creating buttons

button1 = Button(root,text="1",padding=10,command=lambda: button_click(1))
button2 = Button(root,text="2",padding=10,command=lambda: button_click(2))
button3 = Button(root,text="3",padding=10,command=lambda: button_click(3))
button4 = Button(root,text="4",padding=10,command=lambda: button_click(4))
button5 = Button(root,text="5",padding=10,command=lambda: button_click(5))
button6 = Button(root,text="6",padding=10,command=lambda: button_click(6))
button7 = Button(root,text="7",padding=10,command=lambda: button_click(7))
button8 = Button(root,text="8",padding=10,command=lambda: button_click(8))
button9 = Button(root,text="9",padding=10,command=lambda: button_click(9))
button0 = Button(root,text="0",padding=10,command=lambda: button_click(0))
buttonEq = Button(root,text="=",padding=10,command = button_equal,style='E.TButton')
buttonAdd = Button(root,text="+",padding=10,command=build_add)
buttonSub = Button(root,text="-",padding=10,command=button_sub)
buttonMul = Button(root,text="*",padding=10,command=button_mul)
buttonDiv = Button(root,text="/",padding=10,command=button_div)
buttonClear = Button(root,text="Clear",padding=10,command=button_clear,style='C.TButton')

Style().configure('TButton', font =('Comic Sans MS', 20, 'bold'), borderwidth = '4',background = 'light blue')
Style().configure('E.TButton', foreground = 'green')
Style().configure('C.TButton', foreground = 'red')

# screen display
# line 1
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)
#2
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
#3
button7.grid(row=4,column=0)
button8.grid(row=4,column=1)
button9.grid(row=4,column=2)
#4
button0.grid(row=5,column=0)
buttonEq.grid(row=5,column=1)
buttonClear.grid(row=5,column=2)

buttonAdd.grid(row=2,column=4)
buttonSub.grid(row=3,column=4)
buttonMul.grid(row=4,column=4)
buttonDiv.grid(row=5,column=4)



root.mainloop()
