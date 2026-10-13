# ============================================================
# LOOPS
# ============================================================

# Loops are used to execute a block of code repeatedly.
#
# Main types of loops in Python:
# 1. while loop
# 2. for loop


# ============================================================
# 1. WHILE LOOP
# Print 1 to 5
# ============================================================

# i = 1
#
# while i <= 5:
#     print(i)
#     i += 1


# ============================================================
# 2. WHILE LOOP
# Print 5 to 1
# ============================================================

# i = 5
#
# while i >= 1:
#     print(i)
#     i -= 1


# ============================================================
# 3. MULTIPLICATION TABLE
# ============================================================

# n = int(input("Enter a Number: "))
#
# i = 0
#
# while i < 10:
#     print(n * (i + 1))
#     i += 1


# ============================================================
# 4. BREAK
# Stop the loop when number is a multiple of 6
# ============================================================

# i = 1
#
# while i <= 10:
#
#     if i % 6 == 0:
#         break
#
#     print(i)
#     i += 1
#
# print("Outside Loop now...")


# ============================================================
# 5. CONTINUE
# Skip multiples of 3
# ============================================================

# i = 1
#
# while i <= 10:
#
#     if i % 3 == 0:
#         i += 1
#         continue
#
#     print(i)
#     i += 1


# ============================================================
# 6. CONTINUE
# Print only odd numbers from 1 to 10
# ============================================================

# i = 0
#
# while i < 10:
#
#     i += 1
#
#     if i % 2 == 0:
#         continue
#
#     print(i)


# ============================================================
# 7. FOR LOOP
# Loop through a string
# ============================================================

# word = "artificial intelligence"
#
# for ch in word:
#     print(ch)


# ============================================================
# 8. COUNT THE NUMBER OF 'i's
# ============================================================

# word = "Artificial Intelligence"
#
# count = 0
#
# for ch in word:
#     if ch == "i":
#         count += 1
#
# print ("Count of i & I:", count)

# ============================================================
# 9. COUNT VOWELS IN A STRING
# ============================================================

# word = "artificial intelligence"
#
# count = 0
#
# for ch in word:
#     if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#         count += 1
#
# print("The vowel count inside string is", count)


# ============================================================
# 10. RANGE()
# ============================================================

# range(5)
# Gives: 0, 1, 2, 3, 4

# for i in range(5):
#     print(i)


# range(1, 6)
# Gives: 1, 2, 3, 4, 5

# for i in range(1, 6):
#     print(i)


# range(1, 10, 2)
# Gives: 1, 3, 5, 7, 9

# for i in range(1, 10, 2):
#     print(i)


# ============================================================
# 11. SUM OF FIRST N NATURAL NUMBERS
# ============================================================

# n = int(input("Enter a number: "))
#
# sum = 0
#
# for i in range(1, n + 1):
#     sum += i
#
# print("Sum =", sum)


# ============================================================
# 12. NESTED LOOPS
# A loop inside another loop
# ============================================================

# for i in range(1, 3):
#
#     for j in range(1, 3):
#         print(f"({i}, {j})")