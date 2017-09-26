print("\nListing 7.8: Parameter Passing")
print("\nThis program demonstrates passing a parameter from a called function.\n")
def increment(x):
    print("Beginning execution of increment, x =", x)
    x +=1       # Increment x
    print("Ending execution of increment, x =", x)

def main():
    x = 5
    print("Before increment, x =", x)
    increment(x)
    print("After increment, x =", x)

main()

print("\nNOTE: variable x in main is unaffected by increment because x references an integer, and all integers are immutable.")