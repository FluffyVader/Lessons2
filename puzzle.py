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

def update_puzzle ():
    tur.clear()
    draw_puzzles()
 #   sc.update()


def generate_puzzle ():
    numbers = list ( range ( 1 , max_number)) + [ None ]
    random.shuffle(numbers)
    return [numbers[i:i + screen_size] for i in range ( 0 , len (numbers), screen_size)]


def move_left():      
    y, x =  find_empty_tile()
    if x > 0:

        value = puzzles[x-1][y]
        puzzles[x][y] = value
        puzzles[x-1][y] = None
        draw_puzzle_title_none(x-2, y-1)
        draw_puzzle_title(x-1,y-1,value)

def move_right():
    y, x =  find_empty_tile()
    if x < 2:

        value = puzzles[x+1][y]
        puzzles[x][y] = value
        puzzles[x+1][y] = None
        draw_puzzle_title_none(x,y-1)
        draw_puzzle_title(x-1,y-1,value)
def move_up():      
    y, x =  find_empty_tile()
    if y > 0:

        value = puzzles[x][y-1]
        puzzles[x][y] = value
        puzzles[x][y-1] = None
        draw_puzzle_title_none(x-1,y-2)
        draw_puzzle_title(x-1,y-1,value)

def move_down():      
    y, x =  find_empty_tile()
    if y < 2:

        value = puzzles[x][y+1]
        puzzles[x][y] = value
        puzzles[x][y+1] = None
        draw_puzzle_title_none(x-1, y)
        draw_puzzle_title(x-1,y-1,value)
sc.listen() 
sc.onkey(move_left, "a") 
sc.onkey(move_right, "d") 
sc.onkey(move_up, "w")
sc.onkey(move_down, "s")

def finnish_game():
    number = 1
    for i in range(0,3,1):
        for j in range(0,3,1):
            if puzzles[i][j] != number:
                return
    tur.goto(0,0)
    
    tur.pendown()
    tur.write("You win",align = "center", font = ("Arial", 50 , "normal "))

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

def find_empty_tile():
    for y in range (screen_size):
        for x in range (screen_size):
            if puzzles[y][x] is None :
                return x, y


#draws a puzzle tile with a number on it on the puzzle canvas
def draw_puzzle_title(x,y,number):
    global puzzle, puzzles
    startX = 0-x*puzzle_size
    startY = y*puzzle_size  
    tur = turtle.Turtle()
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
    tur.hideturtle()
    tur.end_fill()
    tur.penup()
    
    tur.goto(startX+puzzle_size/2,startY+puzzle_size/2-50)
    
    tur.pendown()
    tur.write(str(number), align = "center", font = ("Arial", 50 , "normal "))

def draw_puzzles():
    for i in range(int(max_number ** 0.5)):

        for j in range(int(max_number ** 0.5)):
            if puzzles[i][j]!= None:
                
                draw_puzzle_title(i-1,j-1,puzzles[i][j])
            else:
                draw_puzzle_title_none(i-1,j-1)
                
def draw_puzzle_title_none(x,y):
    global puzzle, puzzles
    startX = 0-x*puzzle_size
    startY = y*puzzle_size  
    tur = turtle.Turtle()
    tur.penup()
    tur.goto(startX,startY)
    tur.pendown()
    tur.color("white")
    tur.begin_fill()
    for i in range(4):
        tur.forward(puzzle_size)
        tur.left(90)
    tur.end_fill()
    tur.color("red")
    tur.hideturtle()
    tur.end_fill()
    tur.penup()
    
                #def move_left(list0):
# the program starts in the line below.
draw_puzzle()


puzzles = generate_puzzle()

draw_puzzles()

print(puzzles)

sc.mainloop()
