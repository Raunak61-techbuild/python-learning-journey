# ============================================================
# JSON IN PYTHON
# ============================================================

import json

# JSON stands for JavaScript Object Notation.
# Python provides the json module to work with JSON data.


# ============================================================
# 1. JSON STRING TO PYTHON OBJECT
# ============================================================

# json_str = '{"name": "Shradha", "isTeacher": true}'
#
# py_obj = json.loads(json_str)
#
# print(type(py_obj), py_obj)


# ============================================================
# 2. PYTHON OBJECT TO JSON STRING
# ============================================================

# py_obj = {
#     "name": "Shradha",
#     "isTeacher": True
# }
#
# json_str = json.dumps(py_obj)
#
# print(type(json_str), json_str)


# ============================================================
# 3. READING JSON FROM A FILE
# ============================================================

# with open("data.json", "r") as f:
#     py_obj = json.load(f)
#     print(type(py_obj), py_obj)


# ============================================================
# 4. WRITING JSON TO A FILE
# ============================================================

# data = {
#     "name": "Shradha",
#     "age": 27,
#     "isTeacher": True
# }
#
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4, sort_keys=True)



