from .operations import *


def calculate_expression(expression):
    number1, operator, number2 = expression.split(" ")
    result = 0
    if operator == "/":
        result = divide(number1, number2)
    elif operator == "*":
        result = multiply(number1, number2)
    elif operator == "-":
        result = subtract(number1, number2)
    elif operator == "+":
        result = add(number1, number2)
    elif operator == "^":
        result = power(number1, number2)
    return result
