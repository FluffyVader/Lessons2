import turtle, random
puzzle_size = 100
screen_size = 3
width_ = 300
height_ = 300
max_number = 9
missing_puzzle = 8
random_var = random.sample(range(1,max_number),max_number - 1)
sc = turtle.Screen()
tur = turtle.Turtle()
tur.speed(100)
sc.clearscreen()
sc.bgcolor("black")
sc.setup(width = width_, height = height_)
sc.title("puzzle")
puzzles = []
number_of_puzzles = []





def move_up():      ###
    if missing_puzzle != 1 and 4 and 7:
        global puzzles
        y = puzzles[missing_puzzle - 1].ycor() + puzzle_size
        puzzles[missing_puzzle - 1].sety(y)
#def move_down():    ###
#    y = paddA.ycor() - 20 
#    if y < -160:
#        y = -160 
#    paddA.sety(y) 
#def move_left():      ###
#   y = paddB.ycor() + 20 
#    if y > 160:
#       y = 160 
#   paddB.sety(y) 
#def move_right():    ####
#    y = paddB.ycor() - 20 
#    if y < -160:
#        y = -160 
#   paddB.sety(y)



sc.listen() 
sc.onkey(move_up, "Up") 
#sc.onkey(move_down, "Down") 
#sc.onkey(move_right, "Right")
#sc.onkey(move_left, "left")




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
    global puzzle, puzzles
    startX = 0-x*puzzle_size
    startY = y*puzzle_size  
    puzzle = turtle.Turtle()
    puzzle.penup()
    puzzle.goto(startX,startY)
    puzzle.pendown()
    puzzle.color("grey")
    puzzle.begin_fill()
    for i in range(4):
        puzzle.forward(puzzle_size)
        puzzle.left(90)
    puzzle.end_fill()
    puzzle.color("red")
    puzzle.hideturtle()
    puzzle.end_fill()
    puzzle.penup()
    
    puzzle.goto(startX+puzzle_size/2,startY+puzzle_size/2-50)
    
    puzzle.pendown()
    puzzle.write(str(number), align = "center", font = ("Arial", 50 , "normal "))
    puzzles += [puzzle]
    
#def move_left(list0):
# the program starts in the line below.
draw_puzzle()





number = 0
for i in range(int(max_number ** 0.5)):

    for j in range(int(max_number ** 0.5)):
        if number < max_number -1:
            
            draw_puzzle_tile(i-1,j-1,random_var[number])
            number += 1 




sc.mainloop()