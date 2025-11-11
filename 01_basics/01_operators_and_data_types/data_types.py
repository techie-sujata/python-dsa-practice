"""
Topic: Python Data Types
Goal: understand different data types and basic operations

Covers:
- int, float, bool
- string
- list, tuple, set, dict
"""

# numeric
a, b = 10, 3.5
print("a:", a, type(a))
print("b:", b, type(b))
print("sum:", a + b)

# boolean
x = True
y = False
print("x:", x, type(x))
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# string
s = "hello"
print("s:", s, type(s))

# list
ex_list = [1, 2, 3]
print("list:", ex_list, type(ex_list))

# tuple
ex_tuple = (1, 2, 3)
print("tuple:", ex_tuple, type(ex_list))

# set
ex_set = {1, 2, 2, 3}
print("set:", ex_set)  # removes duplicates

# dictionary
ex_dict = {"name": "sujata", "role": "developer"}
print("dict:", ex_dict)
print("keys:", list(ex_dict.keys()))
print("values:", list(ex_dict.values()))
