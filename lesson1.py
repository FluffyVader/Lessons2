
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


answer = Sum(1,5.5)
answer_minus = Minus(9,8)
answer_Divide = Divide(20,5)
answer_remainder = Remainder(4,3)
answer_multipluy = Multipluy(10,10.0)

print(F"The result of invoking Sum(1,5.5) is {answer}")

print(f"The result of invoking Minus(9,8) is {answer_minus}")

print(F"The result of invoking Multipluy(10,10) is {answer_multipluy}")


print(F"The result of invoking Divide(20,5) is {answer_Divide}")

print(F"The result of invoking Remainder(4,3) is {answer_remainder}")
