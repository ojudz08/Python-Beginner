print('\nListing 2.1: Variable')
x = 10
print('x = ', x) #This is an assignment system x = 10

print('\nListing 2.2: Multiple Assigment')
print('-Assigns different values x then directly prints x')
x = 10
print(x)
x = 20
print(x)
x = 30
print(x)

print('\nListing 2.3: Multiple Assignment 2')
print('-Assigns different values x then print using command print("x = " + str(x))')
x = 10
print('x = ' + str(x))
x = 20
print('x = ' + str(x))
x = 30
print('x = ' + str(x))

print('\nListing 2.4: Multiple Assigment')
print('-Assigns different values x then print using command print("x = ", x)')
x = 10
print('x = ', x)
x = 20
print('x = ', x)
x = 30
print('x = ', x)

print('\nListing 2.5: Tuple Assign')
print('-A tuple is a comma-separated list of expressions. Sample belos is a tuple. Assign x, y & z with 100, -45 & 0, respectively.')
x, y, z = 100, -45, 0
print('x =', x, ' y =', y, ' z =', z)
print('\nNote: x, y, z on the code is a tuple and 100, -45 and 0 is another tuple. The first variable in the tuple on the left side corresponds to the assigned tuple on the right side.')

print('\nListing 2.6: Changeable Type')
print('-Assign "a" with int 10 then change it to string ABC')
a = 10
print('First, variable a has value', a, 'and type', type(a))
a = 'ABC'
print('Now, variable a has a value', a, 'and type', type(a))