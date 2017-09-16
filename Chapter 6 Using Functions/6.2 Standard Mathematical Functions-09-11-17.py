print('\nListing 6.3: Calculate the Orbit Distance')
print('Problem: Suppose a spacecraft is at a fixed location in space some distance from a planet. The satellite is orbiting the planet in a circular orbit. Compute how much farther away the sattelite will be from the spacecraft when it has progressed 10 degrees along its orbital path.')
print('\nSee Figure 6.2 Page 130 of the book.')
from math import sqrt, sin, cos, pi # Call functions and values from math package
p_x = 100   # Fixed point location is always (100, 0) --> (px_, p_y)
p_y = 0
radians = 10 * pi/180   # Convert 10 deg to radians
COS10 = cos(radians)    # Get cos of 10 deg
SIN10 = sin(radians)    # Get sine of 10 deg
x, y = eval(input('Enter initial satellite coordinates (x,y): '))
d1 = sqrt((p_x - x)*(p_x - x) + (p_y - y)*(p_y - y)) # Compute the initial distance d1
x_old = x;  # Remember original value of x
x = x*COS10 - y*SIN10   # Compute new x value
y = x_old*SIN10 + y*COS10  # x's value changes but y's value is dependent on x's original value
d2 = sqrt((p_x - x)*(p_x - x) + (p_y - y)*(p_y - y))   # Compute new distance d2
print('Difference in distances: %.3f' % (d2-d1))

print('\nListing 6.4: More Efficient Primes - Improved Efficiency of Listing 5.21')
# No need to call from math import sqrt
max_value = eval(input('Display primes up to what value? '))
value = 2    # Smallest prime number
while value <= max_value:
    is_prime = True   # Check if value is prime, True when value is prime
    trial_factor = 2
    root = sqrt(value)
    while trial_factor <= root:
        if value % trial_factor == 0:
            is_prime = False;   # Found a factor
            break               # Stop when value is not prime
        trial_factor += 1       # Try the next potentiall factor
    if is_prime:
        print(value, end= ' ')  # Display the prime number
    value += 1                  # Try the next potential prime number
print()