#python calculator

operator = input("Enter an operator (+, -, *, /): ")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            exit()
    else:
        print("Invalid operator")
        exit()

    print(f"{num1} {operator} {num2} = {round(result)}")

except ValueError:
    print("Please enter valid numbers.")