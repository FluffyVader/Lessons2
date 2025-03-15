#the user inputs from what time the timer counts down from
import time
number_to_start_from = int(input("enter a number to start from "))

for i in range(number_to_start_from,0,-1):
    print(i)
    time.sleep(1)
print("finished the timer")