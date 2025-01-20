import tkinter
from tkinter import *
Window = Tk()

Window.title("Calculator")

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

def on_button_clicked(btn_text):
    global text
    text += btn_text
    print(text)

def draw_button(x, y, width, height, button_text, button_colour, text_color):
    button1 = screen.create_rectangle(x, y, x + width, y + height, fill = button_colour )
    text = screen.create_text(x+width/2,y+height/2,font="Arial 28",text=button_text, fill=text_color)
    screen.tag_bind(button1, "<Button-1>", lambda _, btn_text = button_text: on_button_clicked(btn_text))


width_of_screen = 2000
height_of_screen = 2000
bgcolor = "White"
init_button_x = 100
init_button_y = 100
button_margin_x = 10
button_margin_y = 10
screen = Canvas(Window,width = width_of_screen, height = height_of_screen, bg = bgcolor)
screen.pack()


button_size = 100
button_colour = "Black"
text_color = "Yellow"
##X = 100
#Y = 100
#button1 = screen.create_rectangle(X,Y,X + button_size,Y + button_size,fill = button_colour )
#screen.tag_bind(button1, "<Button>", draw_button1)
text = ""


draw_button(init_button_x,                                      init_button_y,    button_size,    button_size,    "1",    button_colour,  text_color)
draw_button(init_button_x+button_size+button_margin_x,          init_button_y,    button_size,    button_size,    "2",    button_colour,  text_color)
draw_button(init_button_x+button_size*2+button_margin_x*2,      init_button_y,    button_size,    button_size,    "3",    button_colour,  text_color)
draw_button(init_button_x+button_size*3+button_margin_x*3,      init_button_y,    button_size,    button_size,    "4",    button_colour,  text_color)
draw_button(init_button_x+button_size*4+button_margin_x*4,      init_button_y,    button_size,    button_size,    "5",    button_colour,  text_color)
draw_button(init_button_x+button_size*5+button_margin_x*5,      init_button_y,    button_size,    button_size,    "6",    button_colour,  text_color)
draw_button(init_button_x+button_size*6+button_margin_x*6,      init_button_y,    button_size,    button_size,    "7",    button_colour,  text_color)
draw_button(init_button_x+button_size*6+button_margin_x*7,      init_button_y,    button_size,    button_size,    "8",    button_colour,  text_color)
draw_button(init_button_x+button_size*7+button_margin_x*8,      init_button_y,    button_size,    button_size,    "9",    button_colour,  text_color)
draw_button(init_button_x+button_size*8+button_margin_x*9,      init_button_y,    button_size,    button_size,    "0",    button_colour,  text_color)

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

Window.mainloop()