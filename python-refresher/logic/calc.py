# -----------------------Simple Calculator----------------------
num1 = float(input('Enter num 1: \n'))
num2 = float(input("Enter num 2: "))
operand  = input('Enter  (-, +, /, *)\n')


if operand =="+":
    result = num1 + num2
elif operand == "-":
    result = num1 - num2
elif operand == "*":
    result = num1 * num2
elif operand == "/":
    if num2 !=0:
        result = num1 / num2   
    else:
        result = "Error  division by zero"
else:
    result = "Invalid operand"  



final_result = round(result,1)
print('Result:',final_result)


