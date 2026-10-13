# ============================================================
# EXCEPTION HANDLING
# ============================================================

# An exception is an error that occurs while a program is
# running. If it is not handled, the program may crash.


# ============================================================
# 1. TRY-EXCEPT
# ============================================================

# try:
#     x = 10 / 0
#     print(x)
#
# except:
#     print("Error occurred!")


# ============================================================
# 2. HANDLING SPECIFIC EXCEPTIONS
# ============================================================

# try:
#     print(10 / 0)
#
# except ZeroDivisionError:
#     print("You can't divide by zero!")


# ============================================================
# 3. ELSE BLOCK
# ============================================================

# The else block executes when no exception occurs.

# try:
#     x = int(input("Enter a number: "))
#
# except ValueError:
#     print("Invalid input")
#
# else:
#     print("You entered:", x)


# ============================================================
# 4. FINALLY BLOCK
# ============================================================

# The finally block executes whether an exception occurs or not.

# try:
#     f = open("Sample.txt", "r")
#     print(f.read())
#
# except FileNotFoundError:
#     print("File not found!")
#
# finally:
#     print("Execution completed.")

