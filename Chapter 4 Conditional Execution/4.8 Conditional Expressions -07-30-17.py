print('\nListing 4.14: Save Divide')
dividend, divisor = eval(input('Enter dividend, divisor: '))
# Divide only if divisor =! zero, otherwise print error message
if divisor != 0:
    print(dividend/divisor)
else:
    print('Error, cannot divide by zero')

print('\nListing 4.15: Save Divide Conditional')
dividend, divisor = eval(input('Enter dividend, divisor: '))
# Divide only if divisor =! zero, otherwise print error message
# Shortcut way of coding Listing 4.14
msg = dividend/divisor if divisor !=0 else 'Error, cannot divide by zero'
print(msg)

print('\nListing 4.16: Abs Value Conditional')
# Gets the absolute valeu of a number
n = eval(input('Enter a number: '))
print('|', n, '| = ', (-n if n < 0 else n), sep='')

