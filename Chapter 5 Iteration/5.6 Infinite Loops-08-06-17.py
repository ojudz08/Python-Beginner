print('\nListing 5.16: Find Factors While')
print('This is infinite loop and modified by removing 1 tab on factor line 11')
MAX = 20
n =1
while n <= MAX:
    factor = 1
    print(end=str(n) + ': ')
    while factor <= n:
        if n % factor == 0:
            print(factor, end=' ')
        factor += 1
    print()
    n += 1

print('\nEdited Listing 5.16')
MAX = 20
n =1
while n <= MAX:
    factor = 1
    print(end=str(n) + ': ')
    while factor <= n:
        print('factor =', factor, ' n =', n)
        if n % factor == 0:
            print(factor, end=' ')
        factor += 1
    print()
    n += 1

print('\nListing 5.16: Find Factors for ')
MAX = 20
for n in range(1, MAX + 1):
    print(end=str(n) + ': ')
    for factor in range(1, n + 1):
        if n % factor == 0:
            print(factor, end=' ')
    print()