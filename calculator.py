#https://github.com/AntVa0403/lab11--AV---AV-/blob/main/calculator.py
#partner 1: Anthony Vargas
#partner 2: Anthony Vargas
import math

def add(a, b):
    """Return a + b."""
    return a + b

def square_root(a):
    """Return the square root of a. Raise ValueError if a < 0."""
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    """Return the hypotenuse given sides a and b."""
    return math.hypot(a, b)

def subtract(a, b):
    """Return a - b."""
    return a - b

def mul(a, b):
    """Return a * b."""
    return a * b

def div(a, b):
    """Return a / b. Raise ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError
    return a / b

def logarithm(a, b):
    """Return logarithm of b with base a. Raise ValueError if invalid."""
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)

def exp(a, b):
    """Return a raised to the power of b."""
    return a ** b



