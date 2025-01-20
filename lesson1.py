import tkinter
from tkinter import *
TK = Tk()

TK.title("Culculator")

def Minus(a,b):
    minus = a-b
    return minus

def Multipluy(a,b):
    multipluy = a*b
    return multipluy

def Divide(a,b):
    divide = a/b
    return divide

def Remainder(a,b):
    remainder = a%b
    return remainder

def Sum(a,b):
    sum = a+b
    return sum

def draw_button1():
    global text
    text+= "1"


width_of_screen = 1000
height_of_screen = 1000
bgcolor = "White"

screen = Canvas(TK,width = width_of_screen, height = height_of_screen, bg = bgcolor)
screen.pack()
text = screen.create_text(100,100,font="Arial 18",text="1")
button_size = 100
X = 100
Y = 100
button_colour = "Black"
button1 = screen.create_rectangle(X,Y,X + button_size,Y + button_size,fill = button_colour )
screen.tag_bind(button1, "<Button>", draw_button1)


number_1 = 0 
symbol = "-"
number_2 = 0

answer = 0.0


if symbol == "+":
    answer = Sum(number_1,number_2)

elif symbol == "-":
    answer = Minus(number_1,number_2)

elif symbol == "%":
    answer = Remainder(number_1,number_2)

elif symbol == "*":
    answer = Multipluy(number_1,number_2)

elif symbol == "/":
    answer = Divide(number_1,number_2)

else:
    print(f"the symbol is not a symbol: {symbol}")


print(F"The result of the method is is {answer}")

TK.mainloop()