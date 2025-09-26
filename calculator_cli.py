# calculator_cli.py
from calculator import add, subtract, multiply, divide, sqrt, power, modulus, factorial, sin, cos, log
import math

def main():
    print("Welcome to the Calculator CLI!")
    print("Operations: add, subtract, multiply, divide, sqrt, power, modulus, factorial, sin, cos, log")
    
    op = input("Enter operation: ").strip().lower()
    
    try:
        if op in ["add", "subtract", "multiply", "divide"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if op == "add":
                print("Result:", add(a, b))
            elif op == "subtract":
                print("Result:", subtract(a, b))
            elif op == "multiply":
                print("Result:", multiply(a, b))
            elif op == "divide":
                print("Result:", divide(a, b))
                
        elif op == "sqrt":
            a = float(input("Enter number: "))
            print("Result:", sqrt(a))
            
        elif op == "power":
            a = float(input("Enter base number: "))
            b = float(input("Enter exponent: "))
            print("Result:", power(a, b))
            
        elif op == "modulus":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", modulus(a, b))
            
        elif op == "factorial":
            a = int(input("Enter an integer: "))
            print("Result:", factorial(a))
            
        elif op == "sin":
            a = float(input("Enter angle in degrees: "))
            print("Result:", sin(a))
            
        elif op == "cos":
            a = float(input("Enter angle in degrees: "))
            print("Result:", cos(a))
            
        elif op == "log":
            a = float(input("Enter number: "))
            base_input = input("Enter base (press Enter for 10): ").strip()
            base = float(base_input) if base_input else 10
            print("Result:", log(a, base))
            
        else:
            print("Invalid operation")
            
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
