while True:
    try:
        number_1 = float(input("What is the first number?: "))
        number_2 = float(input("What is the second number?: "))
        operator = input("How would you like to calculate your numbers (+, -, *, /)? ")

        if operator == "+":
            result = number_1 + number_1
        elif operator == "-":
            result = number_1 - number_2
        elif operator == "*":
            result = number_1 * number_2
        elif operator == "/":
            result = number_1 / number_2
        else:
            result = "Unknown operation. Please choose again"
        print(result)
    except ZeroDivisionError:
        print("Error")
