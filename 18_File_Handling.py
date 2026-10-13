# ============================================================
# FILE HANDLING
# ============================================================

# Opening a file
# Syntax: open("filename", "mode")
#
# Modes:
# "r" -> Read
# "w" -> Write (overwrites existing content)
# "a" -> Append (adds content at the end)


# ============================================================
# 1. READING A FILE
# ============================================================

# To read all the contents of a file

# f = open("Sample.txt", "r")
# content = f.read()
# print(content)
# f.close()


# ============================================================
# 2. READING LINES ONE BY ONE
# ============================================================

# f = open("Sample.txt", "r")
#
# line1 = f.readline()
# line2 = f.readline()
#
# print(line1)
# print(line2)
#
# f.close()


# ============================================================
# 3. READING LINES INTO A LIST
# ============================================================

# readlines() returns the lines as a list.

# f = open("Sample.txt", "r")
# lines = f.readlines()
# print(lines)
# f.close()


# ============================================================
# 4. WRITING TO A FILE
# ============================================================

# "w" mode overwrites existing content.

# f = open("Sample.txt", "w")
#
# f.write("Hello Guys! I Eliminated Everything")
# f.write(" But I have included this new text for you Guys")
#
# f.close()


# ============================================================
# 5. WRITING MULTIPLE LINES
# ============================================================

# "a" mode appends content to the file.

# f = open("Sample.txt", "a")
# f.writelines(["Line 1\n", "Line 2\n"])
# f.close()


# ============================================================
# 6. USING WITH
# ============================================================

# The with statement automatically closes the file.

# with open("Sample.txt", "r") as f:
#     data = f.read()
#     print(data)


# ============================================================
# 7. DELETING A FILE
# ============================================================

# import os
#
# os.remove("Sample.txt")


# ============================================================
# 8. SEARCHING FOR A PARTICULAR WORD
# ============================================================

# Search for a word and display the line where it appears.

# data = True
# line = 1
# word = "Python"
#
# with open("Sample.txt", "r") as f:
#     while data:
#         data = f.readline()
#
#         if word in data:
#             print(f"{word} found at line {line}")
#             break
#
#         line += 1
#
# Note: If the word is not found, this code prints nothing.


