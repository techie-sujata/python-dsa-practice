"""
Topic: Python Arithmetic Operators
Goal: practice arithmetic operations and understand precedence

Covers:
- addition (+)
- subtraction (-)
- multiplication (*)
- division (/)
- floor division (//)
- modulus (%)
- exponentiation (**)
"""
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))

# Addition
print("Addition (A+B): ", a + b)

# Subtraction
print("Subtraction (A-B): ", a - b)

# Multiplication
print("Multiplication (A*B): ", a * b)

# Division
print("Division (A/B): ", a / b)

# Floor Division:it divides and returns the largest integer less than or equal to the result
print("Floor Division (A//B): ", a // b)
print("Floor Division (-A//B): ", -a // b)
print("Floor Division (A//-B): ", a // -b)
print("Floor Division (-A//-B): ", -a // -b)

# Modulus: it returns the remainder after division
print("Modulus (A%B): ", a % b)

# Exponentiation: it raises A to the power of B
print("Exponentiation (A**B): ", a ** b)
print("Exponentiation (B**A): ", b ** a)
print("Exponentiation (-A**B): ", -a ** b)
print("Exponentiation (A**-B): ", a ** -b)
print("Exponentiation (-A**-B): ", -a ** -b)
print("Exponentiation (-A**-B): ", -5 ** -(1/2))
