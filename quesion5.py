# prints the numbers between the numbers that the user has given with the step of 1

a = int(input("please enter a number to add:         "))
b = int(input("please enter a number to add:         "))
if a > b:
    for index in range(b,a + 1,1):
        print(index)
elif b > a:
    for index in range(a,b + 1,1):
        print(index)
else:
    print("sorry cant calulate the number")
