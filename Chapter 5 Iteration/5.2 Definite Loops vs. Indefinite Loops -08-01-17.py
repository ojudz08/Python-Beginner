print('\nListing 5.5: Definite 1')
print(' Print integers from 1 to 10.')
n = 1
while n<= 10:
    print(n)
    n += 1

print('\nListing 5.6: Definite 2')
print(' Print integers from 1 to N then stop at N', end='')
n = 1
stop = int(input('Print integers up to what number? '))
while n<= stop:
    print(n)
    n += 1

print('\nListing 5.7: Indifinite')
print(' Sample of indifinite loop wherein entry is set to max 999', end='')
done = False
while not done:
    entry = eval(input('Print integers up to what number? Max 999.'))
    if entry == 999:
        done = True
    else:
        print(entry)