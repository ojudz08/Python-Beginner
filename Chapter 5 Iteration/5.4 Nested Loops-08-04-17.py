print('\nListing 5.8: Times Table')
print(' 10x10 Multiplication Table')
print("       1  2  3  4  5  6  7  8  9 10")
print("    +------------------------------")
product = 0
for row in range(1, 11):
    if row < 10:
        print('', end='')
    print(row, ' | ', end='')
    for column in range(1, 11):
        product = row*column;
        if product <  100:
            print(end=' ')
        if product < 10:
            print(end=' ')
        print(product, end='')
    print()


print('\nListing 5.9: Flexible Times Table')
MAX = 18
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
    print(end="%2i | " % row)
    for column in range(1, MAX + 1):
        product = row+column;
        print(end="%3i " % product)
    print()


print('\nListing 5.10: Permute abc')
print('\nCombination of A B and C')
for first in 'ABC':
    for second in 'ABC':
        if second != first:
            for third in 'ABC':
                if third != first and third != second:
                    print(first + second + third)

print('\nListing 5.10: Permute abcd')
print('\nCombination of A B C and D')
for first in 'ABCD':
    for second in 'ABCD':
        if second != first:
            for third in 'ABCD':
                if third != first and third != second:
                    for fourth in 'ABCD':
                        if fourth != first and fourth != second and fourth != third:
                            print(first + second + third + fourth)