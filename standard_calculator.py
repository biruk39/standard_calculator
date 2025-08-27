
import math
import os

def calculator():
    print("Standard Calculator (Improved)")
    history = []
    try:
        while True:  
            op = input("\nEnter operation (+, -, *, /, sin, cos, tan, sqrt, log, ln, pow, exp, fact, clear, history) or type exit: ").lower()
            if op == "exit":
                print("Exiting the calculator")
                break

            list_op = ["+", "-", "/", "*", "sin", "cos", "tan", "sqrt", "log", "ln", "pow", "exp", "fact", "clear", "history"]
            if op not in list_op:
                print("Please enter a valid operator")
                continue

            if op == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            if op == "history":
                if history:
                    print("Calculation History:")
                    for h in history:
                        print(h)
                else:
                    print("No calculations yet.")
                continue

            if op in ["sin", "cos", "tan", "sqrt", "log", "ln", "exp", "fact"]:
                try:
                    number = float(input("Enter number: "))
                    if op == "sin":
                        result = math.sin(math.radians(number))
                        print(f"sin({number}) = {result}")
                    elif op == "cos":
                        result = math.cos(math.radians(number))
                        print(f"cos({number}) = {result}")
                    elif op == "tan":
                        result = math.tan(math.radians(number))
                        print(f"tan({number}) = {result}")
                    elif op == "sqrt":
                        if number < 0:
                            print("Error: Cannot take square root of a negative number!")
                            continue
                        result = math.sqrt(number)
                        print(f"√{number} = {result}")
                    elif op == "log":
                        if number <= 0:
                            print("Error: log(x) only works for x > 0")
                            continue
                        result = math.log10(number)
                        print(f"log({number}) = {result}")
                    elif op == "ln":
                        if number <= 0:
                            print("Error: ln(x) only works for x > 0")
                            continue
                        result = math.log(number)
                        print(f"ln({number}) = {result}")
                    elif op == "exp":
                        result = math.exp(number)
                        print(f"e^{number} = {result}")
                    elif op == "fact":
                        if number < 0 or not number.is_integer():
                            print("Error: Factorial only works for non-negative integers!")
                            continue
                        result = math.factorial(int(number))
                        print(f"{int(number)}! = {result}")
                    history.append(f"{op}({number}) = {result}")
                except ValueError:
                    print("Invalid input! Please enter a number.")

            elif op == "pow":
                try:
                    base = float(input("Enter base (x): "))
                    exp = float(input("Enter exponent (y): "))
                    result = math.pow(base, exp)
                    print(f"{base}^{exp} = {result}")
                    history.append(f"{base}^{exp} = {result}")
                except ValueError:
                    print("Invalid input! Please enter numbers.")

            else:
                numbers = []
                while True:
                    number = input("Enter number or = to calculate: ")
                    if number == "=":
                        if len(numbers) < 2:
                            print("Enter at least 2 numbers!")
                            continue
                        break
                    try:
                        num = float(number)
                        numbers.append(num)
                    except ValueError:
                        print("Enter numbers only!")
                        continue

                result = numbers[0]
                expression = f"{numbers[0]}"
                if op == "+":
                    for number in numbers[1:]:
                        result += number
                        expression += f" + {number}"
                elif op == "-":
                    for number in numbers[1:]:
                        result -= number
                        expression += f" - {number}"
                elif op == "*":
                    for number in numbers[1:]:
                        result *= number
                        expression += f" * {number}"
                elif op == "/":
                    for number in numbers[1:]:
                        if number == 0:
                            print("Error: Division by zero!")
                            result = None
                            break
                        result /= number
                        expression += f" / {number}"
                if result is not None:
                    print(f"{expression} = {result}")
                    history.append(f"{expression} = {result}")

    except Exception as e:
        print(f"Invalid operation: {e}")

    print("\nDeveloped by: Biruk Daniel")
    print("you are exited from calculator.")

calculator()
