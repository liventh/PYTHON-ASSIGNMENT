def my_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation! Use +, -, *, or /.")
            return
        
        print(f"Result: {num1} {operation} {num2} = {result}")
    except ValueError:
        print("Please enter valid numbers.")

my_calculator()