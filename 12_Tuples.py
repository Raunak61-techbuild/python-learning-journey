# ============================================================
# TUPLES
# ============================================================

# A tuple is an ordered, immutable collection of items.

#String -> " "
#List -> []
#Tuple -> ()
#Dictionary -> {
#Sets -> {}

# ============================================================
# CREATING A TUPLE
# ============================================================

# tup = (10, 20, 30)
# print(tup)
# print(type(tup))


# Single-element tuple
# A comma is required.

# single_element_tuple = (42,)
# print(single_element_tuple)


# ============================================================
# TUPLE CHARACTERISTICS
# ============================================================

# 1. ORDERED
# 2. IMMUTABLE
# 3. ALLOWS DUPLICATES
# 4. HETEROGENEOUS


# ============================================================
# ACCESSING TUPLE ELEMENTS
# ============================================================

# t = (10, 20, 30, 40)

# print(t[0])
# print(t[-1])
# print(t[1:4])


# ============================================================
# LOOPS ON TUPLE
# ============================================================

# t = (10, 20, 30, 40)
#
# for val in t:
#     print(val)


# ============================================================
# SUM OF ALL ELEMENTS IN A TUPLE
# ============================================================

t = (5 , 10 , 15)
sum = 0

for value in t:
    sum += value

print(f"sum is {sum}")


# ============================================================
# TUPLE METHODS
# ============================================================

# index(val)
# Returns the index of the first occurrence of a value.

# count(val)
# Returns the total number of occurrences of a value.


# t = (1, 2, 2, 3, 5)

# print(t.index(2))
# print(t.count(2))