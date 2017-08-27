print('\nExercise 9. Counts the number of asterisk based on the code below')
a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print('*', end='')
        b +=1
    print()
print('Answer: Infinite')