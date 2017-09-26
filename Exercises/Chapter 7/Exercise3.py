print("\nExercise 3. Is the following a legal Python program?\n")
print("def proc(x):")
print("    print(x + 2)\n")
print("def main():")
print("    x = proc(5)\n")
print("main()\n")

def proc(x):
    print(x + 2)
def main():
    x = proc(5)

main()

print("\nYes, the program print the value of x which is 7.")