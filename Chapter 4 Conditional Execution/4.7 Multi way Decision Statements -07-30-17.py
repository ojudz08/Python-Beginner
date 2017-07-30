print('\nListing 4.11: Digit to Word')
print('Uses the if else statement')
value = eval(input('Please enter an integer value in the range 0...5: '))
if value < 0:
    print('Too small')
else:
    if value == 0:
        print('zero')
    else:
        if value == 1:
            print('one')
        else:
            if value == 2:
                print('two')
            else:
                if value == 3:
                    print('three')
                else:
                    if value == 4:
                        print('four')
                    else:
                        if value == 5:
                            print('five')
                        else:
                            print('Too large')
print('Done')

print('\nListing 4.12: Restyled Digit to Word')
print('Uses the if elif else statement, works the same as Listing 4.11')
value = eval(input('Please enter an integer in the range 0...5: '))
if value < 0:
    print('Too small')
elif value == 0:
    print('zero')
elif value == 1:
    print('one')
elif value == 2:
    print('two')
elif value == 3:
    print('three')
elif value == 4:
    print('four')
elif value == 5:
    print('five')
else:
    print('Too large')
print('Done')

print('\nListing 4.13: Date Transformer')
print('Converts numeric month to string month using the if elif else statement')
month = eval(input('Please enter the month as a number (1-12): '))
day = eval(input('Please enter the day of the month: '))

if month == 1:
    print('January ', end='')
elif month == 2:
    print('February ', end='')
elif month == 3:
    print('March ', end='')
elif month == 4:
    print('April ', end='')
elif month == 5:
    print('May ', end='')
elif month == 6:
    print('June ', end='')
elif month == 7:
    print('July ', end='')
elif month == 8:
    print('August ', end='')
elif month == 9:
    print('September ', end='')
elif month == 10:
    print('October ', end='')
elif month == 11:
    print('November ', end='')
else:
    print('December ', end='')

print(day, 'or', day, end='')
if month == 1:
    print(' Enero')
elif month == 2:
    print(' Febrero')
elif month == 3:
    print(' Marzo')
elif month == 4:
    print(' Abril')
elif month == 5:
    print(' Mayo')
elif month == 6:
    print(' Junio')
elif month == 7:
    print(' Julio')
elif month == 8:
    print(' Agosto')
elif month == 9:
    print(' Septiembre')
elif month == 10:
    print(' Octubre')
elif month == 11:
    print(' Noviember')
else:
    print(' Deciembre')