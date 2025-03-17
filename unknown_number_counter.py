start_number = int(input("please enter a start number in here "))

for index in range(start_number,0,-1):
    result_str = str(index)
    result_str += " "
    for i in range(0,index,1):
        result_str += str(index)
    print(result_str)