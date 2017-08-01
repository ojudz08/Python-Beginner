print('\nListing 5.1: Count to Five')
print(' Counting to five by printing the number on each output line')
print(1)
print(2)
print(3)
print(4)
print(5)

print('\nListing 5.2: Iterative to Five')
print(' Uses while loop to count to five')
count = 1
while count <= 5:
    print(count)
    count += 1
    
print('\nListing 5.3: Add Non Negative')
print('Exits when negative values are inputed and then sums all non negative values')
entry = 0  # Initialize, make sure loop is entered
sum = 0    # Intialize sum
print('\nEnter numbers to sum, negative number ends list: ')
while entry >= 0:
    entry = eval(input())
    if entry >= 0:
        sum += entry
print('Sum = ', sum)

"""
print('\nListing 5.4: Troubleshoot Loop')
print('Troubleshooting computer using while loop')
print("\nHelp! My computer doesn't work!")
done = False    # Initialize the code done to set to False
while not done:
    print("Does the computer make any sounds (fans, etc.) ", end='')
    choice = input("or show any lights? (y/n): ")
    if choice == 'n':
        print('Plug it in.')
    else:
        choice = input("Is the switch in the \"on\" position? (y/n): ")
        if choice == 'n':
            print('Turn it on.')
        else:
            choice = input("Does the computer have a fuse? (y/n): ")
            if choice == 'n':
                choice = input("Is the outlet OK? (y/n): ")
                if choice == 'n':
                    print("Chec the outlet's circuit")
                    print("breaker or fuse. Move to a")
                    print("new outlet, if necessary")
                else:
                    print("Please consult a service technican.")
                    done = True
            else:
                print("Check the fuse. Replace if necessary.")
else:
    print("Please consult a service technician.")
    done = True
"""