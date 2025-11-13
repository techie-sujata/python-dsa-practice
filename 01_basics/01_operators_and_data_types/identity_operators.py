"""
Topic: Identity Operators in Python
Goal: understand and practice identity operations to compare object identities

Covers:
- is: checks if two variables point to the same object in memory
- is not: checks if two variables point to different objects in memory
"""

# Example usage of identity operators with integers
a = 1000
b = 1000
print("Identity Operators with Integers A and B:", a, b)
# Check if A and B refer to the same object
print("A is B: ", a is b)
# Check if A and B refer to different objects
print("A is not B: ", a is not b)

# Example usage of identity operators with strings
str1 = "hello"
str2 = "hello"
print("Identity Operators with Strings str1 and str2:", str1, str2)
# Check if str1 and str2 refer to the same object
print("str1 is str2: ", str1 is str2)
# Check if str1 and str2 refer to different objects
print("str1 is not str2: ", str1 is not str2)
str2 = "hello world"
print("Identity Operators with Strings str1 and modified str2='hello world':", str1, str2)
# Check if str1 and str2 refer to the same object
print("str1 is str2: ", str1 is str2)
# Check if str1 and str2 refer to different objects
print("str1 is not str2: ", str1 is not str2)
str2 = "world"
print("Identity Operators with Strings str1 and modified str2='world':", str1, str2)
# Check if str1 and str2 refer to the same object
print("str1 is str2: ", str1 is str2)
# Check if str1 and str2 refer to different objects
print("str1 is not str2: ", str1 is not str2)

# Example usage of identity operators with lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("Identity Operators with Lists list1 and list2:", list1, list2)
# Check if list1 and list2 refer to the same object
print("list1 is list2: ", list1 is list2)
# Check if list1 and list2 refer to different objects
print("list1 is not list2: ", list1 is not list2)
# Assign list1 to list3
list3 = list1
print("Identity Operators with Lists list1 and list3 after list3 = list1:", list1, list3)
# Check if list1 and list3 refer to the same object
print("list1 is list3: ", list1 is list3)
# Check if list1 and list3 refer to different objects
print("list1 is not list3: ", list1 is not list3)

# Example usage of identity operators with dictionaries
dict1 = {"key": "value"}
dict2 = {"key": "value"}
print("Identity Operators with Dicts dict1 and dict2:", dict1, dict2)
# Check if dict1 and dict2 refer to the same object
print("dict1 is dict2: ", dict1 is dict2)
# Check if dict1 and dict2 refer to different objects
print("dict1 is not dict2: ", dict1 is not dict2)
dict3 ={"key1": "value1"}
print("Identity Operators with Dicts dict1 and modified dict3 after dict3 ={'key1': 'value1'}:", dict1, dict3)
# Check if dict1 and dict3 refer to the same object
print("dict1 is dict3: ", dict1 is dict3)
# Check if dict1 and dict3 refer to different objects
print("dict1 is not dict3: ", dict1 is not dict3)
dict3 = dict1
print("Identity Operators with Dicts dict1 and modified dict3 again after dict3 = dict1:", dict1, dict3)
# Check if dict1 and dict3 refer to the same object
print("dict1 is dict3: ", dict1 is dict3)
# Check if dict1 and dict3 refer to different objects
print("dict1 is not dict3: ", dict1 is not dict3)
