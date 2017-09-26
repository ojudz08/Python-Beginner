print("\nExercise 5. Is the following a legal Python program?\n")
print("def proc(x, y):")
print("    return 2*x + y*y\n")
print("def main():")
print("    print(proc(5, 4))\n")
print("main()\n")

def proc(x, y):
    return 2*x + y*y
def main():
    print(proc(5, 4))

main()

print("\nYes, the program calls the formal parameter x & y, pass it to the function proc, then prints the value 26.")