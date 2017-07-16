print('\nLisitng 4.5: Better Feedback')
dividend, divisor = eval(input('Please enter two numbers to divide: '))
if divisor != 0:
    print(dividend, '/', divisor, '=', dividend/divisor)
else:
    print('Division by zero is not allowed')
    
print('\nListing 4.6: Same different')
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print('d1 =', d1, ' d2 = ', d2)
if d1 == d2:
    print('Same')
else:
    print('Different')
