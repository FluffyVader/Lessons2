# the point of the homework was: to input a number and the "#" symbol 1 less time every time the number gets printed
start_number = int(input("please enter a starting number "))

# for index in range(start_number,0,-1):
#     result_str = str(index)
#     hashtag_symbol = "#"
#     result_str += " "
#     result_str += hashtag_symbol*index
    
#     print(result_str)



for index in range(start_number,0,-1):
    result_str = str(index)
    result_str += " "
    for index in range(0,index,1):
        result_str += "#"
    print(result_str)

