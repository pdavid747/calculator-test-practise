# Calculator Project

## Overview
This project implements a **simple calculator** in Python, supporting basic arithmetic operations and square root calculations. It also includes a **test suite** using **pytest** to verify that each operation works correctly. This project is ideal for practicing **unit testing**, **automation testing**, and integration into **CI/CD pipelines** like Jenkins.

---

## Files
- **calculator.py** – contains the implementation of calculator functions.  
- **test_.py** – contains test cases for each calculator function using pytest.

---

## Calculator Functions

### 1. `add(a, b)`
- **Purpose:** Returns the sum of two numbers.  
- **Input:** Two numbers (`a` and `b`).  
- **Output:** Sum of `a` and `b`.  
- **Example:**  
```python
add(2, 3)  # returns 5

### 2. `subtract(a, b)`
- **Purpose:** Returns the difference between two numbers.  
- **Input:** Two numbers (`a` and `b`).  
- **Output:** Result of `a - b`.  
- **Example:**  
```python
subtract(5, 3)  # returns 2

### 3. `multiply(a, b)`
- **Purpose:** Returns the product of two numbers.  
- **Input:** Two numbers (`a` and `b`).  
- **Output:** Product of `a` and `b`.  
- **Example:**  
```python
multiply(3, 4)  # returns 12
multiply(-2, 5) # returns -10


### 4. `divide(a, b)`
- **Purpose:** Returns the result of dividing `a` by `b`.  
- **Input:** Two numbers (`a` and `b`).  
- **Output:** Result of `a / b`.  
- **Edge Case:** Raises a `ValueError` if `b` is 0.  
- **Example:**  
```python
divide(10, 2)  # returns 5
divide(5, 2)   # returns 2.5
divide(10, 0)  # raises ValueError: Cannot divide by zero


### 5. `sqrt(a)`
- **Purpose:** Returns the square root of a number.  
- **Input:** A number `a`.  
- **Output:** Square root of `a`.  
- **Example:**  
```python
sqrt(4)   # returns 2
sqrt(16)  # returns 4



