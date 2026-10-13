# ============================================================
# STRINGS
# ============================================================

# Strings are immutable - they can't be changed or assigned new values after they are created.

# str1 = "hello world"
# str2 = "Prime"


# ============================================================
# LENGTH OF A STRING
# ============================================================

# len() - returns the number of characters in a string

# word = "Prime"
# print(len(word))


# ============================================================
# STRING CONCATENATION
# ============================================================

# Concatenation means combining two or more strings.

# str1 = "hello world"
# str2 = "Prime"
#
# word = str1 + " " + str2
# print(word)


# ============================================================
# LOOPS ON STRING
# ============================================================

# We can use a for loop to access every character
# of a string one by one.

# s = "Python"
#
# for ch in s:
#     print(ch)


# ============================================================
# STRING INDEXING
# ============================================================

# Indexing represents the position of individual characters.
# Index starts from 0.

# s = "Python"
#
# print(s[0])  # P
# print(s[2])  # t
# print(s[3])  # h
# print(s[4])  # o


# ============================================================
# STRING SLICING
# ============================================================

# Slicing lets us access multiple characters at once.

# Syntax:
# string[start : stop : step]
#
# start -> default is 0
# stop  -> stopping position (not included)
# step  -> default is 1

# s = "Python"
#
# print(s[0:2])   # Stop element will not be printed
# print(s[2:])
# print(s[:3])
# print(s[::2])   # Pto
# print(s[::-1])  # Reverse print


# ============================================================
# STRING FORMATTING
# ============================================================

# String formatting is the process of creating dynamic
# strings by inserting values from variables or expressions
# into a predefined string template.


# ------------------------------------------------------------
# 1. Using .format()
# ------------------------------------------------------------

# name = "Rahul"
# age = 25
#
# text = "My name is {} and my age is {}".format(name, age)
# print(text)


# ------------------------------------------------------------
# Positional & Named Placeholders
# ------------------------------------------------------------

# Positional placeholders

text = "Coordinates: {1}, {0}".format("x", "y")
print(text)
# Output: Coordinates: y, x


# Named placeholders

text = "Name: {n}, Age: {a}".format(n="Bob", a=30)
print(text)


# Another positional example

# text = "Name: {1}, Age: {0}".format("Bob", 30)
# print(text)


# ------------------------------------------------------------
# 2. Using f-Strings
# ------------------------------------------------------------

# name = "Rahul"
# age = 25

# text = f"My name is {name} and my age is {age} years old"
# print(text)


# We can also put expressions inside f-strings.

# a = 5
# b = 10
#
# print(f"Sum of {a} & {b} = {a + b}")
# print(f"Avg of {a} & {b} = {(a + b) / 2}")

