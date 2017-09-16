print('\nListing 6.1: Standard Square Root')
print(" This program is the same as Listing 5.18 however using the function sqrt")
print('Note: We will be usign functions from now on/')
from math import sqrt
num = eval(input("Enter number: "))
root = sqrt(num)
print('Square root of', num, '=', root)

print('\nListing 6.2: Using sqrt')
# Different ways to use sqrt
# Note: since math module is called on 6.1, no need to call again in this code
x = 16
print(sqrt(16.0)) # Pass a literal value of x and display result
print(sqrt(x))    # Pass the variable x and display result
print(sqrt(2 * x - 5)) # Pass an expressing, input variable x
y = sqrt(x)            # Assign result to variable  
print(y)
y = 2 * sqrt(x + 16) - 4 # Use result in an expression
print(y)
y = sqrt(sqrt(256.0))    # Use result as an argument to function call
print(y)
print(sqrt(int('45')))