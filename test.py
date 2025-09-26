import pytest
import math
from calculator import (
    add, subtract, multiply, divide, sqrt,
    power, modulus, factorial, sin, cos, log
)

# ---- Addition Tests ----
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# ---- Subtraction Tests ----
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(3, 5) == -2
    assert subtract(5.5, 2.2) == 3.3

# ---- Multiplication Tests ----
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(5, 0) == 0
    assert multiply(2.5, 4.0) == 10.0

# ---- Division Tests ----
def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5
    assert divide(7, 2) == 3.5
    with pytest.raises(ValueError):
        divide(10, 0)

# ---- Square Root Tests ----
def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(16) == 4
    assert math.isclose(sqrt(2), math.sqrt(2))
    with pytest.raises(ValueError):
        sqrt(-1)

# ---- Power Tests ----
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5
    assert power(4, 0.5) == 2

# ---- Modulus Tests ----
def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(20, 7) == 6
    assert modulus(-10, 3) == -10 % 3

# ---- Factorial Tests ----
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-3)

# ---- Trigonometric Tests ----
def test_sin():
    assert math.isclose(sin(0), 0.0, rel_tol=1e-9)
    assert math.isclose(sin(90), 1.0, rel_tol=1e-9)

def test_cos():
    assert math.isclose(cos(0), 1.0, rel_tol=1e-9)
    assert math.isclose(cos(180), -1.0, rel_tol=1e-9)

# ---- Logarithm Tests ----
def test_log():
    assert log(100, 10) == 2
    assert round(log(math.e, 10), 3) == 0.434
    assert log(math.e, math.e) == 1
    with pytest.raises(ValueError):
        log(-1)
