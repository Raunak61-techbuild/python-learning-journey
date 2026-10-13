# ============================================================
# CONDITIONAL STATEMENTS
# ============================================================

# Conditional statements allow the program to make decisions
# based on whether a condition is True or False.
#
# Main conditional statements:
# if
# elif
# else


# ============================================================
# 1. IF - ELSE
# ============================================================

# age = int(input("Enter your age: "))
#
# if age >= 18:
#     print("You can vote")
#     print("You can also get your driving license")
# else:
#     print("You can't vote")
#     print("You can't get your driving license")


# ============================================================
# 2. IF - ELIF - ELSE
# Traffic Light Example
# ============================================================

# colour = input("Enter colour: ")
#
# if colour == "Red":
#     print("STOP")
# elif colour == "GREEN":
#     print("GO")
# elif colour == "YELLOW":
#     print("BE READY")
# else:
#     print("Wrong Colour for Traffic Light")


# ============================================================
# 3. MULTIPLE CONDITIONS
# Using 'and'
# ============================================================
#
# age = int(input("Enter the Age: "))
#
# if age < 13:
#     print("This person is still a child")
# elif age >= 13 and age <= 19:
#     print("This person is a teenager")
# else:
#     print("Adult")


# ============================================================
# 4. NESTED CONDITIONALS
# Login System
# ============================================================

# username = input("Enter a Username: ")
# password = input("Enter a Password: ")
#
# if username == "ADMIN_0123" and password == "MyBottle":
#     print("LOGGED IN SUCCESSFULLY")
#
# else:
#     # First check whether the username is wrong
#     if username != "ADMIN_0123":
#         print("FAILED TO ENTER THE USERNAME")
#     else:
#         # If username is correct, password must be wrong
#         print("FAILED TO ENTER THE PASSWORD")


# ============================================================
# 5. CHECK MULTIPLE OF 5
# ============================================================

# n = int(input("Enter any number: "))
#
# if n % 5 == 0:
#     print("This number is a multiple of 5")
# else:
#     print("This number is not a multiple of 5")


# ============================================================
# 6. CHECK ODD OR EVEN
# ============================================================

# n = int(input("Enter any number: "))
#
# if n % 2 == 0:
#     print("This is an Even Number")
# else:
#     print("This is an Odd Number")


# ============================================================
# 7. TERNARY STATEMENT
# ============================================================

# age = 18
#
# status = "Adult" if age >= 18 else "Not Adult"
#
# print(status)


# ============================================================
# 8. MATCH - CASE
# Python 3.10+
# ============================================================

# colour = input("Enter colour: ")

# match colour:
#     case "Red":
#         print("STOP")
#     case "GREEN":
#         print("GO")
#     case "YELLOW":
#         print("BE READY")
#     case _:
#         print("Wrong Colour")

