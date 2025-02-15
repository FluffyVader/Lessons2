import tkinter
from tkinter import *
Window = Tk()

#init block
number_1 = 0
number_2 = 0
a = ""
b = ""
color1 = "black"
text_sizeY = 100
text_sizeX = 600
list_of_symbols = ["+","-","*","/","%"]
initial_text_field_X = 100
initial_text_field_Y = 100
backspace_symbol = "BSP"
button_size = 100
button_colour = "Black"
text_color = "Yellow"
width_of_screen = 800
height_of_screen = 800
bgcolor = "White"
init_button_x = 100
init_button_y = 250
button_margin_x = 10
button_margin_y = 10
text_to_parse = ""
screen = Canvas(Window,width = width_of_screen, height = height_of_screen, bg = bgcolor)
screen.create_rectangle(button_size, button_size, text_sizeX + button_size, text_sizeY + button_size, fill = color1)
text_view = screen.create_text(initial_text_field_X,    initial_text_field_Y,   font = "Arial 28",  text = text_to_parse,   fill = "white")
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

def draw_text_field(text_param):
    global text_view
    screen.delete(text_view)
    text_view = screen.create_text(initial_text_field_X, initial_text_field_Y,font = "Arial 28", text = text_param, fill = "grey" ,anchor=tkinter.NW)

def on_button_clicked(button_text):
    if button_text == backspace_symbol:
        on_back_space_pressed()
        return

    global text_view, text_to_parse

    text_to_parse += button_text
    draw_text_field(text_to_parse)

def on_button_symbol_clicked(button_text):
    global text_to_parse
    index = 0
    last_symbol =  text_to_parse[len(text_to_parse)-1]
    try:
        index = list_of_symbols.index(last_symbol) 
    except ValueError:
        text_to_parse += button_text
        draw_text_field(text_to_parse)
        
def on_back_space_pressed():
    global text_to_parse

    text_to_parse = text_to_parse[:-1]
    draw_text_field(text_to_parse)



def apply_buttons_horizontal_layout():
    draw_button(init_button_x,                                          init_button_y,    button_size,    button_size,    "1",    button_colour,  text_color)
    draw_button(init_button_x+button_size+button_margin_x,              init_button_y,    button_size,    button_size,    "2",    button_colour,  text_color)
    draw_button(init_button_x+button_size*2+button_margin_x*2,          init_button_y,    button_size,    button_size,    "3",    button_colour,  text_color)
    draw_button(init_button_x+button_size*3+button_margin_x*3,          init_button_y,    button_size,    button_size,    "4",    button_colour,  text_color)
    draw_button(init_button_x+button_size*4+button_margin_x*4,          init_button_y,    button_size,    button_size,    "5",    button_colour,  text_color)
    draw_button(init_button_x+button_size*5+button_margin_x*5,          init_button_y,    button_size,    button_size,    "6",    button_colour,  text_color)
    draw_button(init_button_x+button_size*6+button_margin_x*6,          init_button_y,    button_size,    button_size,    "7",    button_colour,  text_color)
    draw_button(init_button_x+button_size*7+button_margin_x*7,          init_button_y,    button_size,    button_size,    "8",    button_colour,  text_color)
    draw_button(init_button_x+button_size*8+button_margin_x*8,          init_button_y,    button_size,    button_size,    "9",    button_colour,  text_color)
    draw_button(init_button_x+button_size*9+button_margin_x*9,          init_button_y,    button_size,    button_size,    "0",    button_colour,  text_color)
    draw_button(init_button_x+button_size*11+button_margin_x*11,        init_button_y,    button_size,    button_size,    "-",    button_colour,  text_color)
    draw_button(init_button_x+button_size*10+button_margin_x*10,        init_button_y,    button_size,    button_size,    "+",    button_colour,  text_color)
    draw_button(init_button_x+button_size*12+button_margin_x*13,        init_button_y,    button_size,    button_size,    "/",    button_colour,  text_color)
    draw_button(init_button_x+button_size*13+button_margin_x*14,        init_button_y,    button_size,    button_size,    "*",    button_colour,  text_color)
    draw_button(init_button_x+button_size*14+button_margin_x*15,        init_button_y,    button_size,    button_size,    "%",    button_colour,  text_color)
    draw_button_equals (init_button_x+button_size*15+button_margin_x*16,        init_button_y,    button_size,    button_size,    "=",    button_colour,  text_color)

def apply_buttons_2d_layout():
    draw_button(init_button_x,                                                  init_button_y,    button_size,    button_size,    "7",    button_colour,  text_color)
    draw_button(init_button_x+button_size*1+button_margin_x*1,                  init_button_y,    button_size,    button_size,    "8",    button_colour,  text_color)
    draw_button(init_button_x+button_size*2+button_margin_x*2,                  init_button_y,    button_size,    button_size,    "9",    button_colour,  text_color)
    draw_button_symbol(init_button_x+button_size*3+button_margin_x*4,                  init_button_y,    button_size,    button_size,    "*",    button_colour,  text_color)
    draw_button_symbol(init_button_x+button_size*4+button_margin_x*5,                  init_button_y,    button_size,    button_size,    "/",    button_colour,  text_color)
    draw_button(init_button_x,                                                  init_button_y+button_size+button_margin_y,    button_size,    button_size,    "4",    button_colour,  text_color)
    draw_button(init_button_x+button_size*1+button_margin_x*1,                  init_button_y+button_size+button_margin_y,    button_size,    button_size,    "5",    button_colour,  text_color)
    draw_button(init_button_x+button_size*2+button_margin_x*2,                  init_button_y+button_size+button_margin_y,    button_size,    button_size,    "6",    button_colour,  text_color)
    draw_button_symbol(init_button_x+button_size*3+button_margin_x*4,                  init_button_y+button_size+button_margin_y,    button_size,    button_size,    "-",    button_colour,  text_color)
    draw_button_symbol(init_button_x+button_size*4+button_margin_x*5,                  init_button_y+button_size+button_margin_y,    button_size,    button_size,    "+",    button_colour,  text_color)
    draw_button(init_button_x,                                                  init_button_y+button_size*2+button_margin_y*2,    button_size,    button_size,    "1",    button_colour,  text_color)
    draw_button(init_button_x+button_size*1+button_margin_x*1,                  init_button_y+button_size*2+button_margin_y*2,    button_size,    button_size,    "2",    button_colour,  text_color)
    draw_button(init_button_x+button_size*2+button_margin_x*2,                  init_button_y+button_size*2+button_margin_y*2,    button_size,    button_size,    "3",    button_colour,  text_color)
    draw_button_symbol(init_button_x+button_size*3+button_margin_x*4,                  init_button_y+button_size*2+button_margin_y*2,    button_size,    button_size,    "%",    button_colour,  text_color)
    draw_button(init_button_x+button_size*4+button_margin_x*5,                  init_button_y+button_size*2+button_margin_y*2,    button_size,    button_size,    backspace_symbol,    button_colour,  text_color)
    draw_button(init_button_x+button_size*1+button_margin_x*1,                  init_button_y+button_size*3+button_margin_y*3,    button_size,    button_size,    "0",    button_colour,  text_color)
    draw_button(init_button_x+button_size*3+button_margin_x*4,                  init_button_y+button_size*3+button_margin_y*3,    button_size,    button_size,    ".",    button_colour,  text_color)
    
    draw_button_equals(init_button_x+button_size*4+button_margin_x*5,                  init_button_y+button_size*3+button_margin_y*3,    button_size,    button_size,    "=",    button_colour,  text_color)
    



def draw_button_symbol(x, y, width, height, button_text, button_colour, text_color):
    button = screen.create_rectangle(x, y, x + width, y + height, fill = button_colour )
    text = screen.create_text(x+width/2,y+height/2,font="Arial 28",text=button_text, fill=text_color)
    screen.tag_bind(button, 
                    "<Button-1>",
                    lambda _, button_text = button_text: on_button_symbol_clicked(button_text))


def draw_button_equals(x, y, width, height, button_text, button_colour, text_color):
    button1 = screen.create_rectangle(x, y, x + width, y + height, fill = button_colour )
    text = screen.create_text(x+width/2,y+height/2,font="Arial 28",text=button_text, fill=text_color)
    screen.tag_bind(button1, 
                    "<Button-1>",
                    lambda _, btn_text = button_text: on_button_clicked_equals())

def draw_button(x, y, width, height, button_text, button_colour, text_color):
    button1 = screen.create_rectangle(x, y, x + width, y + height, fill = button_colour )
    text = screen.create_text(x+width/2,y+height/2,font="Arial 28",text=button_text, fill=text_color)
    screen.tag_bind(button1, 
                    "<Button-1>",
                    lambda _, btn_text = button_text: on_button_clicked(button_text))
#def culculate(text):
#    global a, b, number_1, number_2
#    symbol = ""
#    for i in text:
#        if i != "+" and i != "-" and i != "%"and i != "*"and i != "/":
#            a += i
#            print(a)
#        else:
#            if symbol == "":
#                symbol = i
#                number_1 = int(a)
#                a = ""
#            else:
#                number_2 = int(a)
#                if symbol == "+":
#                    number_1 = Sum(number_1,number_2)
#                    number_2 = 0
#                    a = ""
#                if symbol == "-":
#                   number_1 = Minus(number_1,number_2)
#                   number_2 = 0
#                    a = ""
#                if symbol == "*":
#                    number_1 = Multipluy(number_1,number_2)
#                    number_2 = 0
#                    a = ""
#                if symbol == "/":
#                    number_1 = Divide(number_1,number_2)
#                    number_2 = 0
#                    a = ""
#                if symbol == "%":
#                    number_1 = Remainder(number_1,number_2)
#                    number_2 = 0
#                    a = ""
#                symbol = i
#    return number_1


def get_number(expression, index):
    num = ""
    while index < len(expression) and (expression[index].isdigit() or expression[index] == "."):
        num += expression[index]
        index += 1
    return float(num), index

def evaluate(expression):
    index = 0
    result, index = get_number(expression, index)
    while index < len(expression):
        operator = expression[index]
        index += 1
        num, index = get_number(expression, index)
        
        if operator == '+':
            result  = Sum(result,num)
        elif operator == '-':
            result = Minus(result,num)
        elif operator == '*':
            result = Multipluy(result,num)
        elif operator == '/':
            result = Divide(result,num)
        elif operator == '%':
            result = Remainder(result,num)
    
    return result
def on_button_clicked_equals():
    global text_view, text_to_parse
    
    screen.delete(text_view)
    answer = evaluate(text_to_parse)
    text_to_parse = f"{answer}"
    text_view = screen.create_text(initial_text_field_X+button_size,    initial_text_field_Y+button_size/2,   font = "Arial 28",  text = text_to_parse,   fill = "red")

screen.pack()
apply_buttons_2d_layout()
Window.mainloop()