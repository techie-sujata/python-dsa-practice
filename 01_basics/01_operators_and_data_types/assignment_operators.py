"""
Topic: Assignment Operators in Python
Goal: understand and practice assignment operations on variables
Covers:
- basic assignment (=): assigns a value to a variable
- addition assignment (+=): adds a value to the variable and assigns the result back to the variable
- subtraction assignment (-=): subtracts a value from the variable and assigns the result back to the variable
- multiplication assignment (*=): multiplies the variable by a value and assigns the result back to the variable
- division assignment (/=): divides the variable by a value and assigns the result back to the variable
- floor division assignment (//=): performs floor division on the variable by a value and assigns the result back to the variable
- modulus assignment (%=): performs modulus operation on the variable by a value and assigns the result back to the variable
- exponentiation assignment (**=): raises the variable to the power of a value and assigns the result back to the variable
- left shift assignment (<<=): performs left bitwise shift on the variable by a value and assigns the result back to the variable
- right shift assignment (>>=): performs right bitwise shift on the variable by a value and assigns the result back to the variable
- bitwise AND assignment (&=): performs bitwise AND on the variable by a value and assigns the result back to the variable
- bitwise OR assignment (|=): performs bitwise OR on the variable by a value and assigns the result back to the variable
- bitwise XOR assignment (^=): performs bitwise XOR on the variable by a value and assigns the result back to the variable
- bitwise NOT assignment (~=): performs bitwise NOT on the variable and assigns the result back to the variable

Note: Assignment operators combine a basic operation with assignment, allowing for more concise code when updating variable values.
"""

# Basic Assignment
a = 80
print("Initial value of a:", a)
# Addition Assignment
a += 5
print("After a += 5:", a)
# Subtraction Assignment
a -= 3
print("After a -= 3:", a)
# Multiplication Assignment
a *= 2
print("After a *= 2:", a)
# Division Assignment
a /= 4
print("After a /= 4:", a)
# Floor Division Assignment
a //= 2
print("After a //= 2:", a)
# Modulus Assignment
a %= 3
print("After a %= 3:", a)
# Exponentiation Assignment
a **= 3
print("After a **= 3:", a)
a = int(a) # converting back to int for bitwise operations
# Left Shift Assignment
a <<= 1
print("After a <<= 1:", a)
# Right Shift Assignment
a >>= 2
print("After a >>= 2:", a)
# Bitwise AND Assignment
a &= 5
print("After a &= 5:", a)
# Bitwise OR Assignment
a |= 2
print("After a |= 2:", a)
# Bitwise XOR Assignment
a ^= 3
print("After a ^= 3:", a)
# Bitwise NOT Assignment
a = ~a
print("After a = ~a:", a)