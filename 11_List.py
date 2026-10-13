# ============================================================
# LISTS
# ============================================================

# A list is a collection of items.

# Lists are:
# 1. Ordered
# 2. Changeable (Mutable)
# 3. Allow duplicates
# 4. Heterogeneous - can contain different data types
# Lists are written using square brackets [].


# ============================================================
# CREATING A LIST
# ============================================================

# my_list = [1, 2, 3, 4, 5]
#
# print(my_list)
# print(type(my_list))


# A list can contain different data types.

# my_list2 = [10, "Hello", 3.14, True, 10]
# print(my_list2)


# ============================================================
# LIST CHARACTERISTICS
# ============================================================

# 1. Ordered
#    Lists have a defined order and can be accessed by index.

# 2. Mutable
#    Lists can be changed after they are created.

# 3. Allows Duplicates
#    The same value can appear more than once.

# 4. Heterogeneous
#    A list can contain different data types.


# ============================================================
# ACCESSING LIST ELEMENTS
# ============================================================

# my_list = ["apple", "banana", "cherry"]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])


# ============================================================
# MODIFYING A LIST
# ============================================================

# my_list = [1, 2, 3, 4]
# my_list[0] = 0
# print(my_list)


# ============================================================
# LENGTH OF A LIST
# ============================================================

# my_list = [7 , 9 , "Raunak"]
# print(len(my_list))

# ============================================================
# LIST SLICING
# ============================================================

# Syntax:
# list[start : end : step]

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(numbers[2:5])
# print(numbers[:4])
# print(numbers[:])
# print(numbers[::2])
# print(numbers[1::3])
# print(numbers[-5:-2])  #NEGATIVE SLICING


# ============================================================
# LIST METHODS
# ============================================================

# len()              -> tells the length
# append(element)    -> adds an element to the end
# insert(index, element) -> adds an element at a specific index
# sort()             -> sorts in ascending/alphabetical order
# reverse()          -> reverses the order


# nums = [5, 2, 9]
# print(len(nums))
#
# nums.append(7)
# print(nums)
#
# nums.insert(1, 4)
# print(nums)
#
# nums.sort()
# print(nums)
#
# nums.reverse()
# print(nums)


# ============================================================
# LOOPS ON LIST
# ============================================================

# We can use a for loop to traverse a list
# element by element.

# numbers = [10, 20, 30, 40, 50]
#
# for num in numbers:
#     print(num)


# ============================================================
# SEARCHING ELEMENTS IN A LIST
# ============================================================

# Search elements one by one.
#
numbers = [4 , 5 , 7 , 8 , 10]

x = 10
indx = 0

for num in numbers:
    if num == x:
        print(f"{x} found at index {indx}")
        break

    indx +=1