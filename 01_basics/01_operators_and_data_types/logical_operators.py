"""
Topic: Logical Operators in Python
Goal: Practice logical operations and understand their usage

Covers:
- logical and
- logical or
- logical not
"""

# Example usage of logical operators using boolean inputs
a = True
b = False
print("Logical Operators with Boolean And B:", a, b)
# Logical AND: True and False -> False
print("A and B: ", a and b)
# Logical OR: True or False -> True
print("A or B: ", a or b)
# Logical NOT: not True -> False
print("not A: ", not a)
# Logical NOT: not False -> True
print("not B: ", not b)

# Example usage of logical operators using integer inputs
x = 5  # non-zero integers are considered True
y = 0  # zero is considered False
print("Logical Operators with Integer X and Y:", x, y)
# Logical AND: 5 and 0 -> 0 (False)
print("X and Y: ", x and y)
# Logical OR: 5 or 0 -> 5 (True)
print("X or Y: ", x or y)
# Logical NOT: not 5 -> False
print("not X: ", not x)
# Logical NOT: not 0 -> True
print("not Y: ", not y)

# Example usage of logical operators using string inputs
str1 = "hello"  # non-empty strings are considered True
str2 = ""       # empty string is considered False
print("Logical Operators with String str1 and str2:", str1, str2)
# Logical AND: "hello" and "" -> "" (False)
print("str1 and str2: ", str1 and str2)
# Logical OR: "hello" or "" -> "hello" (True)
print("str1 or str2: ", str1 or str2)
# Logical NOT: not "hello" -> False
print("not str1: ", not str1)
# Logical NOT: not "" -> True
print("not str2: ", not str2)

# Example usage of logical operators using float inputs
p = 3.5  # non-zero floats are considered True
q = 0.0  # zero is considered False
print("Logical Operators with Float P and Q:", p, q)
# Logical AND: 3.5 and 0.0 -> 0.0 (False)
print("P and Q: ", p and q)
# Logical OR: 3.5 or 0.0 -> 3.5 (True)
print("P or Q: ", p or q)
# Logical NOT: not 3.5 -> False
print("not P: ", not p)
# Logical NOT: not 0.0 -> True
print("not Q: ", not q)

# negative integer case
m = -10  # non-zero integers are considered True
n = 0    # zero is considered False
print("Logical Operators with Negative Integer M and N:", m, n)
# Logical AND: -10 and 0 -> 0 (False)
print("M and N: ", m and n)
# Logical OR: -10 or 0 -> -10 (True)
print("M or N: ", m or n)
# Logical NOT: not -10 -> False
print("not M: ", not m)
# Logical NOT: not 0 -> True
print("not N: ", not n)

# Combined logical operations
# Example: (A and B) or (not A)
result1 = (a and b) or (not a)
# here a=True, b=False => (True and False) or (not True) => False or False => False
print("(A and B) or (not A): ", result1)
# Example: (X or Y) and (not Y)
result2 = (x or y) and (not y)
# here x=5 (True), y=0 (False) => (True or False) and (not False) => True and True => True
print("(X or Y) and (not Y): ", result2)

# mixed type logical operations
q = 5  # non-zero integer is considered True
r = "hello"  # non-empty string is considered True
print("Logical Operators with Mixed Types Q and R:", q, r)
# Logical AND: 5 and "hello" -> "hello" (True) because both are True but returns the last evaluated value
print("Q and R: ", q and r)
# Logical OR: 5 or "hello" -> 5 (True) because first is True
print("Q or R: ", q or r)
# Logical NOT: not 5 -> False because non-zero integer is True
print("not Q: ", not q)
# Logical NOT: not "hello" -> False because non-empty string is True
print("not R: ", not r)