a = int(input("please enter a start number "))
b = int(input("please enter a end number "))
c = int(input("enter a number to try to divide with "))


for i in range(a+1,b,1):
    if i%c == 0:
        print(i)
else:
    print("cant divide")