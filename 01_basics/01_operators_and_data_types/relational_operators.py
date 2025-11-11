"""
Topic: Python Relational/Comparison Operators
Goal: practice relational operations and understand their usage

Covers:
- less than (<)
- greater than (>)
- less than or equal to (<=)
- greater than or equal to (>=)
- equal to (==)
- not equal to (!=)
"""
# Example usage of relational operators using integer inputs
a = int(input("Enter value of integer A: "))
b = int(input("Enter value of integer B: "))
# a=5 and b=3
# Less than: 5 is not less than 3 -> False
print("A < B: ", a < b)
# Greater than: 5 is greater than 3 -> True
print("A > B: ", a > b)
# Less than or equal to: 5 is not less than or equal to 3 -> False
print("A <= B: ", a <= b)
# Greater than or equal to: 5 is greater than or equal to 3 -> True
print("A >= B: ", a >= b)
# Equal to: 5 is not equal to 3 -> False
print("A == B: ", a == b)
# Not equal to: 5 is not equal to 3 -> True
print("A != B: ", a != b)
# Example usage of relational operators using string inputs
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
# Example: str1="hello", str2="world"
# Less than: first character of "hello" is 'h' and of "world" is 'w', since 'h' comes before 'w' in ASCII, "hello" < "world" -> True
print("str1 < str2: ", str1 < str2)
# Greater than: first character of "hello" is 'h' and of "world" is 'w', since 'h' comes before 'w' in ASCII, "hello" > "world" -> False
print("str1 > str2: ", str1 > str2)
# Less than or equal to: "hello" is less than "world" -> True
print("str1 <= str2: ", str1 <= str2)
# Greater than or equal to: "hello" is not greater than "world" -> False
print("str1 >= str2: ", str1 >= str2)
# Equal to: "hello" is not equal to "world" -> False
print("str1 == str2: ", str1 == str2)
# Not equal to: "hello" is not equal to "world" -> True
print("str1 != str2: ", str1 != str2)
# Example usage of relational operators using float inputs
x = float(input("Enter value of float X: "))
y = float(input("Enter value of float Y: "))
# Example: x=3.0 and y=2.8
# Less than: 3.0 is not less than 2.8 -> False
print("X < Y: ", x < y)
# Greater than: 3.0 is greater than 2.8 -> True
print("X > Y: ", x > y)
# Less than or equal to: 3.0 is not less than or equal to 2.8 -> False
print("X <= Y: ", x <= y)
# Greater than or equal to: 3.0 is greater than or equal to 2.8 -> True
print("X >= Y: ", x >= y)
# Equal to: 3.0 is not equal to 2.8 -> False
print("X == Y: ", x == y)
# Not equal to: 3.0 is not equal to 2.8 -> True
print("X != Y: ", x != y)
# Example usage of relational operators using mixed type inputs
m = int(input("Enter integer value M: "))
n = float(input("Enter float value N: "))
# Example: m=5 and n=5.5
# Less than: 5 is less than 5.5 -> True
print("M < N: ", m < n)
# Greater than: 5 is not greater than 5.5 -> False
print("M > N: ", m > n)
# Less than or equal to: 5 is less than or equal to 5.5 -> True
print("M <= N: ", m <= n)
# Greater than or equal to: 5 is not greater than or equal to 5.5 -> False
print("M >= N: ", m >= n)
# Equal to: 5 is not equal to 5.5 -> False
print("M == N: ", m == n)
# Not equal to: 5 is not equal to 5.5 -> True
print("M != N: ", m != n)
# Note: Comparing different data types (like int and str) will raise a TypeError in Python 3