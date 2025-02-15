import turtle

puzzle_size = 100
screen_size = 3
width_ = 300
height_ = 300
sc = turtle.Screen()
tur = turtle.Turtle()
sc.clearscreen()
sc.bgcolor("black")
sc.setup(width = width_, height = height_)
sc.title("puzzle")



# draws a big white puzzle canvas
def draw_puzzle():
    tur.penup()
    tur.goto(0-puzzle_size,0-puzzle_size)
    tur.pendown()
    tur.color("white")
    tur.begin_fill()
    for i in range(4):

        tur.forward(puzzle_size*3)
        tur.left(90)
    tur.end_fill()

#draws a puzzle tile with a number on it on the puzzle canvas
def draw_puzzle_tile(x,y,number):
    
    startX = 0-x*puzzle_size
    startY = y*puzzle_size
    
    print(f"x:{x}, y:{y}, number:{number}, goto x:{startX}, goto y:{startY}")

    tur.penup()
    tur.goto(startX,startY)
    tur.pendown()
    tur.color("grey")
    tur.begin_fill()
    for i in range(4):
        tur.forward(puzzle_size)
        tur.left(90)
    tur.end_fill()
    tur.color("red")

    tur.penup()
    
    tur.goto(startX+puzzle_size/2,startY+puzzle_size/2)
    
    tur.pendown()
    tur.write(str(number), align = "center", font = ("Arial", 8 , "normal "))

# the program starts in the line below.
draw_puzzle()

number = 1
for i in range(3):
    for j in range(3):
        draw_puzzle_tile(i-1,j-1,number)
        number += 1 


sc.mainloop()
