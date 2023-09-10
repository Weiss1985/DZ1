result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        if wait_for_number:
            user_input = input("Enter a number: ")
            operand = float(user_input)
            if result is None:
                result = operand
            wait_for_number = False
        else:
            user_input = input("Enter an operator (+, -, *, /) or = to calculate: ")
            if user_input == "=":
                break
            elif user_input in ("+", "-", "*", "/"):
                if operator is not None:
                    if operator == "+":
                        result += operand
                    elif operator == "-":
                        result -= operand
                    elif operator == "*":
                        result *= operand
                    elif operator == "/":
                        if operand != 0:
                            result /= operand
                        else:
                            print("Error: Division by zero")
                            continue
                operator = user_input
                wait_for_number = True
            else:
                print("Error: Invalid operator")
                continue
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
if operator is not None:
    if operator == "+":
        result += operand
    elif operator == "-":
        result -= operand
    elif operator == "*":
        result *= operand
    elif operator == "/":
        if operand != 0:
            result /= operand
        else:
            print("Error: Division by zero")

print("Result:", result)
