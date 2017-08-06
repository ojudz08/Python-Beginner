print('\nJust an illustration, not part of the book')
print("Illustrates the for statement --> for n in range(begin, end, step)")
beg, end, step = eval(input('Type the number you want to print, end and the step (separate with comma): '))
for n in range(beg, end, step):
    print('Number/s are ', n, '', end='')


print('\n\nAnother example')
print('Sums the range indicated.')
beg, end, step = eval(input('Type the start, end, step (separate with comma): '))
sum = 0
for i in range(beg, end, step):
    sum += i
print('Sum =', sum)