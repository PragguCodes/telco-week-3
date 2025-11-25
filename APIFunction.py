import logging

# Configure logging
logging.basicConfig(
    filename="calculator_log.txt",
    level=logging.INFO,
)

def calculator(num1, num2, operator):
    logging.info(f"Operation: {num1} {operator} {num2}")

    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2  # may raise ZeroDivisionError
        elif operator == "%":
            result = num1 % num2
        elif operator == "**":
            result = num1 ** num2
        else:
            logging.warning(f"Invalid Operator: {operator}")
            return "Invalid Operator"

        logging.info(f"Result: {result}")
        return result

    except ZeroDivisionError:
        logging.error("Division by Zero Error")
        return "Error: Cannot divide by zero"


# MULTIPLE TEST CASES
print(calculator(10, 5, "+"))
print(calculator(20, 10, "-"))
print(calculator(4, 6, "*"))
print(calculator(12, 4, "/"))
print(calculator(10, 3, "%"))
print(calculator(2, 5, "**"))  # power
print(calculator(10, 0, "/"))   # division error
print(calculator(8, 3, "$"))    # invalid operator


print("Check calculator_log.txt for logs.")
