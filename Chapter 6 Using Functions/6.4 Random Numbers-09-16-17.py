print('\nProgram executes random package --> random, randrange & seed')

print('\nListing 6.10: Simple Random')
from random import randrange, seed

seed(23)                                # Set randowm number seed
for i in range(0, 100):                 # Print 100 random numbers
    print(randrange(1, 1000), end=' ')  # From range 1 to 1000
print()                                 # Print new line

print('\nListing 6.10.1: Modified Simple Random')
print('Modified to input seed number')
# NOTE: No need to call from random import randrange, seed

a = eval(input('Enter seed number: '))  # Asks user to input seed number
max_value = 1000                        # Set max value to 1000
seed(a)                                 # Set randowm number seed
for i in range(0, max_value):           # Print 100 random numbers
    print(randrange(1, 1000), end=' ')  # From range 1 to 1000
print()

print('\nListing 6.11: Die')            # Print new line
# NOTE: No need to call from random import randrange
for i in range(0, 3):           # Roll the dice 3 times
    value = randrange(1, 6)
    
    print('+-------+')
    if value == 1:
        print('|       |')
        print('|   *   |')
        print('|       |')
    elif value == 2:
        print('|*      |')
        print('|       |')
        print('|      *|')
    elif value == 3:
        print('|      *|')
        print('|   *   |')
        print('|*      |')
    elif value == 4:
        print('|*     *|')
        print('|       |')
        print('|*     *|')
    elif value == 5:
        print('|*     *|')
        print('|   *   |')
        print('|*     *|')
    elif value == 6:
        print('|*  *  *|')
        print('|       |')
        print('|*  *  *|')
    else:
        print(' *** Error: illegal die value ***')
    print('+-------+')