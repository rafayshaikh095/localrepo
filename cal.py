def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def modulus(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x % y

def power(x, y):
    return x ** y

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %, ^")
    print("Type 'q' to quit.")

    while True:
        try:
            expression = input("\nEnter expression (example: 10 + 5): ").strip()
        except KeyboardInterrupt:
            print("\nExiting calculator...")
            break

        if expression.lower() == 'q':
            print("Goodbye!")
            break

        parts = expression.split()
        if len(parts) != 3:
            print("Invalid input. Use format: number operator number")
            continue

        num1_str, operator, num2_str = parts

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Please enter valid numbers.")
            continue

        try:
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == '%':
                result = modulus(num1, num2)
            elif operator == '^':
                result = power(num1, num2)
            else:
                print("Unsupported operator.")
                continue

            print(f"Result: {result}")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    calculator()