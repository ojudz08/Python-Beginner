print('\nListing 4.2: Better Division', end='')
# Let the user input dividend and divisor, then set condition to proceed to division process if divisor is not equal to zero
dividend, divisor = eval(input('Please enter two numbers to divide: '))
if divisor != 0:
    print(dividend, '/', divisor, "=", dividend/divisor)


print('\nListing 4.3: Alternate Division', end='')
# Improved division that prints the word 'Program finished'
dividend, divisor = eval(input('Please enter two numbers to divide: '))
if divisor != 0:
    quotient = dividend / divisor
    print(dividend, '/', divisor, "=", quotient)
print('Program finished')

print('\nListing 4.4: Leading zeros', end='')
num = eval(input('Please enter an integer in the range 0... 9999: '))
if num < 0:
    num = 0
if num > 9999:
    num = 9999

print(end='[')          # Left brace

digit = num // 1000
print(digit, end='')
num %= 1000

digit = num // 10
print(digit, end='')
num %= 10

print(num, end='')
print(']')