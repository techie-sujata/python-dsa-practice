"""
Topic: Bitwise Operators in Python
Goal: understand and practice bitwise operations on data types

Covers:
- bitwise AND (&) : performs AND operation on each bit of the numbers and its result is 1 if both bits are 1, otherwise 0
- bitwise OR (|): performs OR operation on each bit of the numbers and its result is 1 if at least one of the bits is 1, otherwise 0
- bitwise XOR (^): performs XOR operation on each bit of the numbers and its result is 1 if the bits are different, otherwise 0
- bitwise NOT (~): inverts all the bits of the number, basically changing 0s to 1s and 1s to 0s
- left shift (<<): shifts the bits of the number to the left by a specified number of positions meaning multiplying the number by 2 for each shift position
- right shift (>>): shifts the bits of the number to the right by a specified number of positions meaning dividing the number by 2 for each shift position

Note: Bitwise operations are typically performed on integer data types.Because bitwise operations work on bits, and:
-Integers have a fixed binary representation.
-Strings and floats don’t have straightforward binary bit-level meanings in this context.
    --String bits represent characters (not numbers).
    --Float bits represent decimal fractions in a complex IEEE 754 format — not useful for normal bit math.
"""

# Example usage of bitwise operators
a = 10  # in binary: 1010
b = 4   # in binary: 0100
print("Bitwise Operators with A and B:", a, b)
# Bitwise AND: 1010 & 0100 -> 0000 (0 in decimal)
print("A & B: ", a & b)
# Bitwise OR: 1010 | 0100 -> 1110 (14 in decimal)
print("A | B: ", a | b)
# Bitwise XOR: 1010 ^ 0100 -> 1110 (14 in decimal)
print("A ^ B: ", a ^ b)
# Bitwise NOT: ~1010 -> 0101 (in 2's complement, this is -11 in decimal) and ~4 -> 1011 (in 2's complement, this is -5 in decimal)
print("~A: ", ~a)
print("~B: ", ~b)
# Left Shift: 1010 << 2 -> 101000 (40 in decimal) and 4 -> 10000 (16 in decimal)
print("A << 2: ", a << 2)
print("B << 2: ", b << 2)
# Right Shift: 1010 >> 2 -> 0010 (2 in decimal) and 4 -> 0001 (1 in decimal)
print("A >> 2: ", a >> 2)
print("B >> 2: ", b >> 2)