def calculate(number, symbol, number2):
    if symbol == "+":
        return number + number2
    elif symbol == "-":
        return number - number2
    elif symbol == "*":
        return number * number2
    elif symbol == "/":
        if number2 == 0:
            return "Error: Division by zero"
        return number / number2
    else:
        return "Invalid operation"

result = float(input("Enter the first number: "))

while True:
    symbol = input("Choose an operation (+, -, *, /): ").strip()
    next_number = float(input("Enter the next number: "))

    result = calculate(result, symbol, next_number)
    print(f"Current result: {result}")

    choice = input("Do you want to continue? (y or n): ").strip().lower()
    if choice != "y":
        print("Final result:", result)
        print("Thanks for using the calculator!")
        break