import math
import logging
import argparse

# Configure logging
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---- Calculator Functions ----
def add(a, b):
    result = a + b
    logging.info(f"ADD {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logging.info(f"SUBTRACT {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logging.info(f"MULTIPLY {a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        logging.error("Attempted division by zero")
        raise ValueError("Cannot divide by zero")
    result = a / b
    logging.info(f"DIVIDE {a} / {b} = {result}")
    return result

def sqrt(a):
    if a < 0:
        logging.error("Attempted sqrt of negative number")
        raise ValueError("Cannot take square root of a negative number")
    result = math.sqrt(a)
    logging.info(f"SQRT {a} = {result}")
    return result

def power(a, b):
    result = a ** b
    logging.info(f"POWER {a}^{b} = {result}")
    return result

def modulus(a, b):
    result = a % b
    logging.info(f"MODULUS {a} % {b} = {result}")
    return result

def factorial(a):
    if a < 0:
        logging.error("Attempted factorial of negative number")
        raise ValueError("Cannot take factorial of a negative number")
    result = math.factorial(a)
    logging.info(f"FACTORIAL {a}! = {result}")
    return result

def sin(a):
    result = math.sin(math.radians(a))
    logging.info(f"SIN({a}) = {result}")
    return result

def cos(a):
    result = math.cos(math.radians(a))
    logging.info(f"COS({a}) = {result}")
    return result

def log(a, base=10):
    if a <= 0:
        logging.error("Attempted log of non-positive number")
        raise ValueError("Logarithm undefined for non-positive numbers")
    result = math.log(a, base)
    logging.info(f"LOG base {base} of {a} = {result}")
    return result


# ---- CLI Interface ----
def main():
    parser = argparse.ArgumentParser(description="Advanced CLI Calculator")
    parser.add_argument("operation", type=str, help="Operation: add, subtract, multiply, divide, sqrt, power, modulus, factorial, sin, cos, log")
    parser.add_argument("numbers", type=float, nargs="*", help="Numbers for the operation")
    args = parser.parse_args()

    try:
        if args.operation == "add":
            print(add(args.numbers[0], args.numbers[1]))
        elif args.operation == "subtract":
            print(subtract(args.numbers[0], args.numbers[1]))
        elif args.operation == "multiply":
            print(multiply(args.numbers[0], args.numbers[1]))
        elif args.operation == "divide":
            print(divide(args.numbers[0], args.numbers[1]))
        elif args.operation == "sqrt":
            print(sqrt(args.numbers[0]))
        elif args.operation == "power":
            print(power(args.numbers[0], args.numbers[1]))
        elif args.operation == "modulus":
            print(modulus(args.numbers[0], args.numbers[1]))
        elif args.operation == "factorial":
            print(factorial(int(args.numbers[0])))
        elif args.operation == "sin":
            print(sin(args.numbers[0]))
        elif args.operation == "cos":
            print(cos(args.numbers[0]))
        elif args.operation == "log":
            if len(args.numbers) == 2:
                print(log(args.numbers[0], args.numbers[1]))
            else:
                print(log(args.numbers[0]))
        else:
            print("Unknown operation")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
