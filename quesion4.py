#prints the numbers from var (20) to the user input
var = 20
while True:
    input1 = int(input(f"enter a number bigger then {var}: "))
    if input1 >var:

        for i in range(var,input1+1,1):
            print(i)
        break
    elif input1 < var:
        print(f"the number is less then {var}")
    else:
        print(f"you cant have the number as {var}")