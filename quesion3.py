#the student enters the amount of test he's taken and the programm calcualtes the average score the student gets 
amountofgrades = 0
inputgrade = int(input("enter the amount "))

for i in range (0,inputgrade,1):
    inputnumber = int(input("enter your grade "))
    amountofgrades += inputnumber
print(f"the average score the student gets: {amountofgrades/inputgrade}")