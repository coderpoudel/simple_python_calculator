num1 = (float(input("Enter first number: ")))
num2 = (float(input("Enter seccond number: ")))

operator = input("Enter the operator +, -, /, *: ")

if operator == '+':
    print(num1 + num2)
    
elif operator == '-':
    print(num1 - num2)
    
elif operator == '*':
    print(num1 * num2)
    
elif operator == '/':
    if num2 > 0:
        print(num1 / num2)
    else:
        print("Syntax error")
        
else:
    print("Enter valid operator")

    
