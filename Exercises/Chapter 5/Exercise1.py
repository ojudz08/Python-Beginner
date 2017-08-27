print('\nExercise 1. Edited Listing 5.3: Add Non Negative')
print('Exits when negative values are inputed and then sums all non negative values')
entry = 0  # Initialize, make sure loop is entered
sum = 0    # Intialize sum
print('\nEnter numbers to sum, negative number ends list: ')
while entry >= 0:
    entry = eval(input())
    if entry > 0:
        sum += entry
print('Sum = ', sum)

print('Answer: Yes, it will achieve the same result. Once 0 is inpute as for >= 0, the total will not chanage. So same as > 0')