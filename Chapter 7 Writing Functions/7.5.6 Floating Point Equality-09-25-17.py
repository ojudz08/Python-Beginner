print("\nListing 7.14: Simple Floating")
def main():
    x = 0.9
    x += 0.1
    if x == 1.0:
        print("OK")
    else:
        print("NOT OK")
        
main ()



print("\nListing 7.15: Bad Float Check")
def main():
    #   Count to ten by tenths
    i = 0.0
    while i != 1.0:
        print("i =", i)
        i += 0.1

main()



print("\nListing 7.16: Float Equals")
from math import fabs

#  equals(a, b, tolerance)
#     Returns true of a = b or |a - b| < tolerance
#     If a and b differ by only a small amount
#     (specified by tolerance), a and b are considered
#     "equal". Useful to account for floating-point
#     round-off error.
#     The == operator is checked first since some special
#     floating-point values such as floating-point infinity
#     require an exact equality check.
def equals(a, b, tolerance):
    return a == b or fabs(a - b) < tolerance;

#  Try out the equals function
def main():
    i = 0.0
    while not equals(i, 1.0, 0.0001):
        print("i =", i)
        i += 0.1

main ()    #  Runs the program