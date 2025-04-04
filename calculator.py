num1 = float(input('Enter first digit: '))
num2 =float(input('Enter second digit: '))
operation = input("Enter the operation (+, -, *, /): ").strip()
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':

    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    result = num1 / num2
else:
    print("Error: Invalid operation! Please use +, -, *, or /")


print(f"{num1} {operation} {num2} = {result}")