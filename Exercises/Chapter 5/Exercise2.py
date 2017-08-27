print('\nExercise 2. Edited Listing 5.3: Add Non Negative')
print('Exits when negative values are inputed and then sums all non negative values')
entry = 0  # Initialize, make sure loop is entered
sum = 0    # Intialize sum
print('\nEnter numbers to sum, negative number ends list: ')
while entry > 0:
    entry = eval(input())
    if entry >= 0:
        sum += entry
print('Sum = ', sum)

print('Answer: No, The program executes and then ends without asking the user to input number. Since entry is initialize to be equal to 0 before the while loop, it did not meet the while statement having > 0 so it ends')