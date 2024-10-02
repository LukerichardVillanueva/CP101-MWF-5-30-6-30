def calculator():
   
    while True:
        # User input
        num1 = input("Enter first number : ")
        if num1.lower() == 'exit':
            break
            
        operation = input("Enter operation (+, -, *, /): ")
        num2 = input("Enter second number: ")

        # Perform calculation
        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    result = "Error! Division by zero."
                else:
                    result = num1 / num2
            else:
                result = "Invalid operation."

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculator()
    
