# ============================================================
# LIST COMPREHENSIONS
# ============================================================

# List comprehensions provide a short and elegant way
# to create lists in Python.

# General syntax:
# [expression for item in iterable]


# ============================================================
# 1. BASIC LIST COMPREHENSION
# ============================================================

# Create a list of numbers from 1 to 5.

# nums = [x for x in range(1, 6)]
# print(nums)


# ============================================================
# 2. LIST COMPREHENSION WITH A CONDITION
# ============================================================

# Syntax:
# [expression for item in iterable if condition]

# Create a list of even numbers from 1 to 10.

# evens = [x for x in range(1, 11) if x % 2 == 0]
# print(evens)


# ============================================================
# 3. LIST COMPREHENSION WITH IF-ELSE
# ============================================================

# Syntax:
# [expression_if_true if condition else expression_if_false
#  for item in iterable]

# Label each number from 1 to 5 as Even or Odd.

# labels = [
#     "Even" if x % 2 == 0 else "Odd"
#     for x in range(1, 6)
# ]
#
# print(labels)

