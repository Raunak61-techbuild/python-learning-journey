# ============================================================
# FUNCTIONS
# ============================================================

# A function is a reusable block of code that performs
# a specific task.
#
# We use:
# def       -> to define a function
# function() -> to call the function
# return    -> to send a result back


# ============================================================
# 1. SIMPLE FUNCTION
# ============================================================

# def hello():
#     print("Hello")
#     print("From Python")
#
#
# # Function call
# hello()


# ============================================================
# 2. FUNCTION WITH PARAMETERS
# Calculate sum of two numbers
# ============================================================

# def calculate_sum (a , b):
#     s = a + b
#     return s
#
# answer = calculate_sum (5, 7)
# print("Sum :", answer)


# ============================================================
# 3. FUNCTION WITH THREE PARAMETERS
# Calculate average of three numbers
# ============================================================

# def calculate_average(a, b, c):
#
#     average = (a + b + c) / 3
#
#     return average
#
#
# answer = calculate_average(3, 4, 5)
#
# print("Average =", answer)


# ============================================================
# 4. DEFAULT PARAMETERS
# ============================================================

# If b is not provided, Python automatically uses 1.

# def add_numbers(a, b=0):
#     return a + b
#
# print(add_numbers(5, 6))
#
# # Here b is not provided, so b = 1
# print(add_numbers(5))


# ============================================================
# 5. LAMBDA FUNCTION
# ============================================================

# Lambda functions are small, one-line functions.
# Syntax:
# lambda arguments: expression

# sum_numbers = lambda a, b: a + b
#
# print("Sum =", sum_numbers(4, 5))


# Lambda function to calculate average
#
# average = lambda a, b: (a + b) / 2
#
# print("Average =", average(4, 5))


# ============================================================
# 6. FACTORIAL FUNCTION
# ============================================================

# def calc_factorial(n):
#
#     fact = 1
#
#     for i in range(1, n + 1):
#         fact *= i
#
#     return fact
#
#
# n = int(input("Enter n: "))
#
# print("Factorial =", calc_factorial(n))


# ============================================================
# 7. LARGEST OF THREE NUMBERS
# ============================================================

# def get_largest(a, b, c):
#
#     if a > b and a > c:
#         return a
#
#     elif b > c:
#         return b
#
#     else:
#         return c
#
#
# print("Largest =", get_largest(3, 10, 5))