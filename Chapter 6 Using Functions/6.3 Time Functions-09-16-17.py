print('\nThe programs executes time and math packages --> clock, sleep and sqrt')

print('\nListing 6.5: Time it')
print('Code calling time package.')
print('This code will measure the response time when you type yout name.\n')
from time import clock, sleep # Use in Listing 6.5 to 6.8, sleep used in Listing 6.9
from math import sqrt  # Use in Listing 6.8 only
print('Enter your name: ', end='')
start_time = clock()
name = input()
elapsed = clock() - start_time
print(name, 'it took you', round(elapsed,2), 'sec to respond.')

print('\nListing 6.6: Time Addition')
print('Measure the time it took the Python program to add up all the integers from 1 to 100M.\n')
# NOTE: No need to call time package and import clock as this was declared above.
sum = 0
n = 0
start = clock()
for n in range(1, 10000001):
    sum += n
elapsed = clock() - start
print('sum:', sum, 'time:', elapsed)

print('\nListing 6.7: Measure Prime Speed')
print('Measures how long it takes the program to count prime numbers up to 10K using same algorithm as Listing 5.22')
# NOTE: No need to call time package and import clock as this was declared above.
max_value = 10000
count = 0
start_time = clock()
for value  in range(2, max_value + 1):   # Try values from 2 smallest prime number to max_value
    is_prime = True                      # Check if value is prime, True if it satisfies the condition
    for trial_factor in range(2, value): # Try all possible factors from 2 to value -1
        if value % trial_factor == 0:
            is_prime = False             # When factor is found
            break
    if is_prime:
        count += 1                       # Count the prime number
print()
elapsed = clock() - start_time
print('Count: ', count, ' Elapsed time: ', elapsed, 'sec')

print('\nListing 6.8: Time More Efficient Primes')
# No need to input from time import clock and from math import sqrt
max_value = 10000
count = 0
value = 2
start = clock()
while value <= max_value:    # Check if the value is prime
    is_prime = True          # True when value is prime
    trial_factor = 2         # Try all possible factors from 2 to value -1
    root = sqrt(value)
    while trial_factor <= root:
        if value % trial_factor == 0:
            is_prime = False;  # Found a factor
            break
        trial_factor += 1
    if is_prime:
        count += 1
    value += 1
elapsed = clock() - start
print('Count: ', count, ' Elapsed time: ', elapsed, 'sec')

print('\nListing 6.9: Countdown')
print('This program runs Countdown from 10 to 1')
# No need to call from time import sleep
for count in range(10, -1, -1):
    print(count)
    sleep(1)