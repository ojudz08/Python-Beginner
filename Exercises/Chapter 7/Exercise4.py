print("\nExercise 4. Is the following a legal Python program?\n")
print("def proc(x):")
print("    print(x + 2)\n")
print("def main():")
print("    proc(5)\n")
print("main()\n")

def proc(x):
    print(x + 2)
def main():
    proc(5)

main()

print("\nYes, the program calls the formal parameter x and pass it to the function proc, then returns the value 7.")