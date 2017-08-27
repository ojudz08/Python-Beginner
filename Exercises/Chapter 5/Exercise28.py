print('\nExercise 28. Modified Listing 5.9 flexibletimestable.py')
print('Modified such that multiplication table depends on the user input.')
MAX = eval(input('Input the maximum row by column:'))
product = 0
print(end='     ')
for column in range(1, MAX + 1):
    print(end=" %2i " % column)
print()
print(end='    +')
for column in range(1, MAX + 1):
    print(end='----')
print()
for row in range(1, MAX + 1):
    print(end="%2i | " % row )
    for column in range(1, MAX + 1):
        product = row*column;
        print(end="%3i " % product)
    print()