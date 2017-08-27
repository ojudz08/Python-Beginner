print("\nExercise 29. A program that accepts a single integer value entered by the user. If the value entered is less than one, the program prints nothing. If the user enters a positive integer, n, the program prints an n×n box drawn with * characters.")
MAX = eval(input('Input the maximum row by column: '))
product = 0
for row in range(1, MAX + 1):
    for column in range(1, MAX + 1):
        product = row*column;
        print('*', end='')
    print()
    
print('\nNote: I just copied the code from Exercise 28 and removed unecessary codes an it works! yey!')