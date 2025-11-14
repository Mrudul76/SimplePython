# GUI  Calculator using Python
# This project emphasis on creating a UI Calculator in Python by utilising the Tkinter python library. 

# Importing required libraries
import tkinter
from tkinter import *  
from tkinter import messagebox  


# Intializing variables

var=""
A=0
operator=""


# Button functions
# We need a total of 16 buttons spread across 4 rows [0-9,+,-,/,*,=,C]

def button_1_is_Clicked():
    global var
    var=var+ "1"
    the_data.set(var)

def button_2_is_Clicked():
    global var
    var=var+ "2"
    the_data.set(var)

def button_3_is_Clicked():
    global var
    var=var+ "3"
    the_data.set(var)

def button_4_is_Clicked():
    global var
    var=var+ "4"
    the_data.set(var)

def button_5_is_Clicked():
    global var
    var=var+ "5"
    the_data.set(var)

def button_6_is_Clicked():
    global var
    var=var+ "6"
    the_data.set(var)

def button_7_is_Clicked():
    global var
    var=var+ "7"
    the_data.set(var)

def button_8_is_Clicked():
    global var
    var=var+ "8"
    the_data.set(var)

def button_9_is_Clicked():
    global var
    var=var+ "9"
    the_data.set(var)

def button_0_is_Clicked():
    global var
    var=var+ "0"
    the_data.set(var)

def button_Add_is_Clicked():
    global A
    global var
    global operator
    A=float(var)
    operator="+"
    var=var+"+"
    the_data.set(var)

def button_Sub_is_Clicked():
    global A
    global var
    global operator
    A=float(var)
    operator="-"
    var=var+"-"
    the_data.set(var)

def button_Mul_is_Clicked():
    global A
    global var
    global operator
    A=float(var)
    operator="*"
    var=var+"*"
    the_data.set(var)

def button_Div_is_Clicked():
    global A
    global var
    global operator
    A=float(var)
    operator="/"
    var=var+"/"
    the_data.set(var)

def button_Equal_is_Clicked():
    global A
    global var
    global operator
    A=float(var)
    operator="="
    var=var+"="
    the_data.set(var)

# C is cancel button in a calculator
def button_C_is_Clicked():
    global A
    global var
    global operator
    A=0
    operator=""
    var=""
    the_data.set(var)

# Defining function to calculate the output.

def result():
    global A
    global operator
    global var
    var2=var
    if operator == "+" :
        value=float((var2.split("+")[1]))
        operation=A+value
        the_data.set(operation)
        var=str(operation)
    elif operator == "-" :
        value=float((var2.split("-")[1]))
        operation=A-value
        the_data.set(operation)
        var=str(operation)
    elif operator == "*" :
        value=float((var2.split("*")[1]))
        operation=A*value
        the_data.set(operation)
        var=str(operation)       
    elif operator == "/" :
        value=float((var2.split("/")[1]))
        if value==0 :
            messagebox.showerror("Division by 0 Not Allowed.")
            A == ""
            var=""
            the_data.set(var)
        else:    
            operation=float(A/value)
            the_data.set(operation)
            var=str(operation)

# Creating the window for GUI Calculator

# Creating an object
guiWindow=tkinter.Tk()

# Setting the window size
guiWindow.geometry("320x600+400+400")

#Disabling the resizable option
guiWindow.resizable(0,0)

# Giving title to the GUI Window
guiWindow.title("Calculator")

# Creating label for the window

the_data=StringVar()
guiLabel=Label(
    guiWindow,
    text="Label",
    anchor=SE,
    font=("Cambria Math",20),
    textvariable=the_data,
    background="#ffffff",
    fg="#000000"
)

#The expand parameter is responsible for the expansion of the parent widget.
guiLabel.pack(expand=True,fill="both")

# Creating frames for the buttons [We should have 4 frames, as it will have 4 rows of buttons]

#First Frame
frameOne=Frame(guiWindow,bg="#000000")
frameOne.pack(expand=True,fill="both")

#Second Frame
frameTwo=Frame(guiWindow,bg="#000000")
frameTwo.pack(expand=True,fill="both")

#Third Frame
frameThird=Frame(guiWindow,bg="#000000")
frameThird.pack(expand=True,fill="both")

#Fourth Frame
frameFourth=Frame(guiWindow,bg="#000000")
frameFourth.pack(expand=True,fill="both")

# Attaching buttons in each frame

# Frame One buttons:
button_1=Button(
    frameOne,
    text="1",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_1_is_Clicked
)
# Aligning buttons to each other in a frame

button_1.pack(side=LEFT,expand=True,fill="both")

button_2=Button(
    frameOne,
    text="2",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_2_is_Clicked
)
button_2.pack(side=LEFT,expand=True,fill="both")

button_3=Button(
    frameOne,
    text="3",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_3_is_Clicked
)

button_3.pack(side=LEFT,expand=True,fill="both")

button_C=Button(
    frameOne,
    text="C",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_C_is_Clicked
)

button_C.pack(side=LEFT,expand=True,fill="both")

button_4=Button(
    frameTwo,
    text="4",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_4_is_Clicked
)
button_4.pack(side=LEFT,expand=True,fill="both")

# Frame Two buttons:
button_5=Button(
    frameTwo,
    text="5",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_5_is_Clicked
)
button_5.pack(side=LEFT,expand=True,fill="both")

button_6=Button(
    frameTwo,
    text="6",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_6_is_Clicked
)
button_6.pack(side=LEFT,expand=True,fill="both")

button_ADD=Button(
    frameTwo,
    text="+",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_Add_is_Clicked
)
button_ADD.pack(side=LEFT,expand=True,fill="both")

# Third Frame buttons:
button_7=Button(
    frameThird,
    text="7",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_7_is_Clicked
)
button_7.pack(side=LEFT,expand=True,fill="both")

button_8=Button(
    frameThird,
    text="8",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_8_is_Clicked
)
button_8.pack(side=LEFT,expand=True,fill="both")

button_9=Button(
    frameThird,
    text="9",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_9_is_Clicked
)
button_9.pack(side=LEFT,expand=True,fill="both")

button_Sub=Button(
    frameThird,
    text="-",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_Sub_is_Clicked
)
button_Sub.pack(side=LEFT,expand=True,fill="both")

# Fourth Frame buttons:
button_0=Button(
    frameFourth,
    text="0",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_0_is_Clicked
)
button_0.pack(side=LEFT,expand=True,fill="both")

button_Mul=Button(
    frameFourth,
    text="*",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_Mul_is_Clicked
)
button_Mul.pack(side=LEFT,expand=True,fill="both")

button_Div=Button(
    frameFourth,
    text="/",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= button_Div_is_Clicked
)
button_Div.pack(side=LEFT,expand=True,fill="both")

button_Equal=Button(
    frameFourth,
    text="=",
    font=("Cambria",22),
    relief=GROOVE,
    border=0,
    command= result
)
button_Equal.pack(side=LEFT,expand=True,fill="both")

#Running the GUI

guiWindow.mainloop()
