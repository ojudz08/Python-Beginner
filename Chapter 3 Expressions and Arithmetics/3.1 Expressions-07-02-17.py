print('\nListing 3.1: Adder')
value1 = int(input('Please enter a number: '))
value2 = int(input('Please enter another number: '))
sum = value1 + value2
print(value1, '+', value2, '=', sum)

print('\nListing 3.2: Imprecise')
one = 1.0
one_third = 1.0/3.0
zero = one - one_third - one_third - one_third
print('one =', one, ' one_third =', one_third, ' zero =', zero)

print('\nListing 3.3: Imprecise 10')
one_tenth = 1.0/10.0
zero = one - one_tenth - one_tenth - one_tenth \
           - one_tenth - one_tenth - one_tenth \
           - one_tenth - one_tenth - one_tenth \
           - one_tenth
print('one = ', one, ' one_tenth =', one_tenth, ' zero =', zero)