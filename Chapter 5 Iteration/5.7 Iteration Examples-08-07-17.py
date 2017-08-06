print('This is what I am waiting for! Practical Applications of if and while statement')
print('\nListing 5.18: Computer Square Root')
print('\n This computes the squre root of a number inputed by user.')
print('  1. Guess the square root.')
print('  2. Square the guess number and check how close it is to the original number, if it is close enough, program stops.')
print('  3. Make a new guess that will produce a better result and proceed with step2.')
print('NOTE: I did put round off statement so I will not confuse myself.')
val = eval(input('Enter number: '))
root = 1.0;
diff = root*root - val
while diff > 0.00000001 or diff < -0.00000001:
    root = (root + val/root) / 2
    print(round(root,2), 'squared is', round(root*root, 2))
    diff = root*root - val
print('Square root of', val, "=", round(root, 2))

print('\nListing 5.19: Start Tree')
print(" This program execute tree's height inputed by user.")
height = eval(input('Enter height of tree: '))
row = 0
while row < height:
    count = 0
    while count < height - row:
        print(end=" ")
        count += 1
    
    count = 0
    while count < 2*row +1:
        print(end="*")
        count += 1
    print()
    row += 1
    
print('\nListing 5.20: Start Tree for')
print(' Tree execution inputted by user using for statement.')
height = eval(input('Enter height of tree: '))
for row in range(height):
    for count in range(height - row):
        print(end=" ")
    for count in range(2*row + 1):
        print(end="*")
    print()

print('\nListing 5.21: Print Prime Numbers While Statement')
print(' This progam execute all prime numbers within the range of the number inputted by user using While Statement')
max_value = eval(input('Display primes up to what value? '))
value = 2
while value <= max_value:
    is_prime = True
    trial_factor = 2
    while trial_factor < value:
        if value % trial_factor == 0:
            is_prime = False;
            break
        trial_factor += 1
    if is_prime:
        print(value, end= ' ')
    value += 1
print()

print('\nListing 5.22: Print Prime Numbers For Statment')
print(' This progam execute all prime numbers within the range of the number inputted by user using For Statement')
max_value = eval(input('Display primes up to what value? '))
for  value in range(2, max_value + 1):
    is_prime = True
    for trial_factor in range(2, value):
        if value % trial_factor == 0:
            is_prime = False
            break
    if is_prime:
        print(value, end= ' ')
print()

print('\nListing 5.23: Better Input Only')
print(' This progam traps the user unless provided with acceptable integer')
in_value = 0
attempts = 0
while in_value < 1 or in_value > 10:
    in_value = int(input('Please enter an integer int he range 0-10: '))
    attempts += 1
tries = 'try' if attempts == 1 else 'tries'
print('It took you', attempts, tries, 'to enter a valid number')