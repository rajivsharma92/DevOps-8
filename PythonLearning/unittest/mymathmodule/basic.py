"""
This module covers functions used for sq-root, cuboid, addition, 
subtraction, multiplication, division, and more will be added in the future.
"""

def add(a, b):
    """
    Calculates the sum of two numbers and returns the result.

    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.

    Returns:
    int/float: The sum of a and b.
    """
    return a + b

def subtract(num1, num2):
    """
    Calculates the difference between two numbers and returns the result.

    Parameters:
    num1 (int/float): The first number.
    num2 (int/float): The second number.

    Returns:
    int/float: The difference between num1 and num2.
    """
    return num1 - num2

def multiply(a, b):
    """
    Calculates the product of two numbers and returns the result.

    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.

    Returns:
    int/float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Calculates the division of two numbers and returns the result.

    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.

    Returns:
    float: The result of dividing a by b.

    Raises:
    ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def square(a):
    """
    Calculates the square of a number and returns the result.

    Parameters:
    a (int/float): The number to be squared.

    Returns:
    int/float: The square of a.
    """
    return a ** 2

def square_root(a):
    """
    Calculates the square root of a number and returns the result.

    Parameters:
    a (int/float): The number to find the square root of.

    Returns:
    float: The square root of a.
    """
    return a ** 0.5
