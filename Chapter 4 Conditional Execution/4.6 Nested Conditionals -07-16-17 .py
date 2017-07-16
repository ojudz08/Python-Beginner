print('\nListing 4.7: Check Range')
value = eval(input('Please enter an integer value in the range 0...10: '))
if value >=0:
    if value <= 10:
        print('In range')
print('Done')

print('\nListing 4.8: New Check Range')
value = eval(input('Please enter an integer value in the range 0...10: '))
if value >=0 and value <= 10:
    print('In range')
print('Done')

print('\nListing 4.9: Enhanced Check Range')
value = eval(input('Please enter an integer value in the range 0...10: '))
if value >= 0:
    if value <= 10:
        print(value, 'is in range')
    else:
        print(value, 'is too large')
else:
    print(value, ' is too small')
print('Done')

print('\nListing 4.10: Troubleshoot')
print("Help! My computer doesn't work!")
print("Does the computer make any sounds (fans, etc.)")
choice = input("or show any lights? (y/n): ")
if choice == 'n':
    choice == input('It is plugged in? (y/n): ')
    if choice == 'n':
        print("Plug it in. If the problem persists, please run this program again.")
    else:
        choice = input("Is the switch in the \"on\" position? (y/n): ")
        if choice == 'n':
            print("Turn it on. If problem persists, please run this program again.")
        else:
            choice == input("Does the computer have a fuse? (y/n): ")
            if choice == 'n':
                choice == input("Is the outlet OK? (y/n): ")
                if choice == 'n':
                    print("Check the outlet's circuit breaker or fuse. Move to a new outlet, if necessary. If problem persists, run this program again.")
                else:
                    print("Please consult a service technician.")
            else:
                print("Check the fuse. Replace if necessary. If the problem persists, then please run this program again.")
else:
    print("Please consult a service technician.")