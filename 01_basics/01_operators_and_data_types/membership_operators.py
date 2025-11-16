"""
Topic: Membership Operators in Python
Goal: understand and practice membership operations to check for presence of elements in collections
Covers:
- in: checks if a value is present in a collection (like list, tuple, set, or string)
- not in: checks if a value is not present in a collection
"""

# Example usage of membership operators with a list
my_list = [10, 20, 30, 40, 50]
print("Membership Operators with List:", my_list)
# Check if 30 is in the list
print("30 in my_list:", 30 in my_list)
# Check if 60 is not in the list
print("60 not in my_list:", 60 not in my_list)
# Example usage of membership operators with a string
my_string = "Hello, welcome to Python programming."
print("Membership Operators with String:", my_string)
# Check if 'Python' is in the string
print("'Python' in my_string:", 'Python' in my_string)
# Check if 'Java' is not in the string
print("'Java' not in my_string:", 'Java' not in my_string)
# Example usage of membership operators with a set
my_set = {1, 2, 3, 4, 5}
print("Membership Operators with Set:", my_set)
# Check if 3 is in the set
print("3 in my_set:", 3 in my_set)
# Check if 6 is not in the set
print("6 not in my_set:", 6 not in my_set)
# Example usage of membership operators with a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Membership Operators with Dictionary:", my_dict)
# Check if 'b' is a key in the dictionary
print("'b' in my_dict:", 'b' in my_dict)
# Check if 2 is a value in the dictionary
print("2 in my_dict.values():", 2 in my_dict.values())
# Check if 'd' is not a key in the dictionary
print("'d' not in my_dict:", 'd' not in my_dict)
# Check if 4 is not a value in the dictionary
print("4 not in my_dict.values():", 4 not in my_dict.values())


