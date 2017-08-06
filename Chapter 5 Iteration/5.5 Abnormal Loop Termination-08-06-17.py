print('\nListing 5.12: Add Middle Exit')
print(' Shows how break statement is used.\n')
entry = 0
sum = 0
print('Enter numbers to sum, negative number ends list: ')
while True:
    entry = eval(input())
    if entry < 0:
        break
    sum += entry
print('Sum =', sum)

print('\nListing 5.13: Troubleshoot Loop2')
print(' Shows how break statement in Computer Problem.\n')
print("Help! My computer doesn't work!")
while True:
    choice = input("Does the computer make any sounds (fans, etc.) or show any lights? (y/n): ")
    if choice == 'n':
        choice = input("Is it plugged in? (y/n): ")
        if choice == 'n':
            print("Plug it in.")
        else:
            choice = input("Is the switch in the \"on\" position? (y/n): ")
            if choice == 'n':
                print("Turn it on.")
            else: 
                choice = input("Does the computer have a fuse? (y/n): ")
                if choice == 'n':
                    choice = input("IS the outlet OK? (y/n): ")
                    if choice == 'n':
                        print("Chec the outlet's circuit ")
                        print("breaker or fuse. Move to a")
                        print("new outlet, if necessary. ")
                    else:
                        print("Please consult a service technician.")
                else:
                    print("Check the fuse. Replace if necessary.")
                    break
    else:
        print("Please consult a service technician.")
        break

print('\nListing 5.14: Continue Example')
print(' Shows how continue statement is used in continuing loop unless condition is met.')
sum = 0
done = False;
while not done:
    val = eval(input('Enter positive integer (999 quits): '))
    if val < 0:
        print('Negative value', val, "ignored")
        continue;
    if val != 999:
        print('Tallying', val)
        sum += val
    else:
        done = (val == 999);
print('sum = ', sum)

print('\nListing 5.15: Non Continue Example')
print(' Same as Listing 5.14 without the continue statement.')
sum = 0
done = False;
while not done:
    val = eval(input('Enter positive integer (999 quits): '))
    if val < 0:
        print('Negative value', val, "ignored")
    if val != 999:
        print('Tallying', val)
        sum += val
    else:
        done = (val == 999);
print('sum = ', sum)