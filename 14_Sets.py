# ============================================================
# SETS
# ============================================================

# A set is an unordered collection of unique elements.


# ============================================================
# CREATING A SET
# ============================================================

# my_set = {1, 2, 2, 2, 3}
#
# print(my_set)
# print(type(my_set))
# print(len(my_set)) #It doesn't count same element twice


# ============================================================
# EMPTY SET
# ============================================================

# To create an empty set, use set().
# {} creates an empty dictionary.

# empty_set = set()
# print(empty_set)


# ============================================================
# SET CHARACTERISTICS
# ============================================================

# 1. Can only have unique elements.

# 2. They are unordered.
#    Therefore, there is no indexing or slicing.

# 3. Sets are mutable.

# 4. Elements inside a set must be immutable.


# ============================================================
# SET METHODS
# ============================================================

# add(element)
# Adds an element to the set.

# remove(element)
# Removes a specific element from the set.

# pop()
# Removes and returns an element from the set.

# clear()
# Removes all elements from the set.


# ============================================================
# ADD
# ============================================================

s = {10, 20, 30}
s.add(40)
print(s)

# ============================================================
# REMOVE
# ============================================================

s.remove(10)
print(s)


# ============================================================
# POP
# ============================================================

# pop() can remove any element because sets are unordered.

print(s.pop())


# ============================================================
# CLEAR
# ============================================================

s.clear()

print(s)


# ============================================================
# UNION & INTERSECTION
# ============================================================

# A = {1, 2, 3}
# B = {3, 4, 5}

# UNION
# Combines elements from both sets.

# print(A.union(B))


# INTERSECTION
# Returns elements common to both sets.

# print(A.intersection(B))