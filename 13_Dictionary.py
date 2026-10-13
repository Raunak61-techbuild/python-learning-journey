# ============================================================
# DICTIONARY
# ============================================================

# A dictionary stores data in key:value pairs.
# Dictionaries are mutable.


# ============================================================
# CREATING A DICTIONARY
# ============================================================

# my_dict = {
#     "name": "Raunak",
#     "age": 19,
#     "city": "Bokaro"
# }
#
# print(my_dict)
# print(type(my_dict))
# print(len(my_dict))


# ============================================================
# DICTIONARY METHODS
# ============================================================

# keys()
# Returns all keys.

# values()
# Returns all values.

# items()
# Returns key-value pairs as tuples.

# get(key)
# Safer way to access the value of a particular key.
# Returns None if the key doesn't exist.

# update(new_item)
# Adds a new item to the dictionary.



# ============================================================
# DICTIONARY METHODS - EXAMPLE
# ============================================================

# d = {
#     "name": "Shraddha",
#     "subjects": ["math", "science", "physics"],
#     "cgpa": 9.5
# }
#
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d.get("cgpa"))


# ============================================================
# UPDATE A DICTIONARY
# ============================================================

# new_item = {"city": "Bokaro"}
#
# print(d.update(new_item))
# print(d)


# ============================================================
# LOOPS ON DICTIONARY
# ============================================================

# d = {
#     "name": "Raunak",
#     "subjects": ["math", "science", "physics"],
#     "cgpa": 9.5
# }
#
# for key, value in d.items():
#     print(key , ":",  value)
