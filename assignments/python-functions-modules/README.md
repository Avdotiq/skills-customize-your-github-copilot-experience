# 📘 Assignment: Python Functions and Modules

## 🎯 Objective

Learn how to write reusable Python functions, organize code into separate modules, and import helper code from another file.

## 📝 Tasks

### 🛠️ Create Reusable Functions

#### Description
Write functions that solve common problems and return values instead of printing directly.

#### Requirements
Completed program should:

- Include a function called `greet_user(name)` that returns a greeting string.
- Include a function called `calculate_rectangle_area(width, height)` that returns the rectangle area.
- Include a function called `is_prime(number)` that returns `True` for prime numbers and `False` otherwise.

### 🛠️ Organize Code into a Module

#### Description
Move helper functions into a separate module file called `helpers.py`, then import those functions into `starter-code.py`.

#### Requirements
Completed program should:

- Create a module file named `helpers.py`.
- Import `greet_user`, `calculate_rectangle_area`, and `is_prime` from `helpers.py` into `starter-code.py`.
- Use those imported functions in a `main()` function inside `starter-code.py`.

### 🛠️ Use Functions Together

#### Description
Write a main program that uses all helper functions and displays clear output.

#### Requirements
Completed program should:

- Call `greet_user()` with a sample name and print the result.
- Call `calculate_rectangle_area()` with width and height values and print the computed area.
- Call `is_prime()` with a sample number and print whether the number is prime.
- Ensure the program only runs the demonstration when `starter-code.py` is executed directly.
