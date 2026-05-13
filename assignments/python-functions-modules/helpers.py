def greet_user(name):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}! Welcome to Python functions and modules."


def calculate_rectangle_area(width, height):
    """Return the area of a rectangle using width and height."""
    return width * height


def is_prime(number):
    """Return True if number is a prime number, otherwise False."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True
