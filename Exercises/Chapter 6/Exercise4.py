print("\nExercise 4. Write a computer program that, given the lengths of the two sides of a right triangle adjacent to the right angle, computes the length of the hypotehuse of the triangle.")
from math import sqrt
a, b = eval(input("Enter values for a & b (the two sides of the right triangle, separate with ,): "))
c = sqrt((a*a)+(b*b))
print("\nAnswer: The hypotenuse of the triangle with side ", a, " and side", b, " is equal to ", round(c, 4), ".")