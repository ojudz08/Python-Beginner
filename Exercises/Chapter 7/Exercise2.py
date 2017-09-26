print("\nExercise 2. Is the following a legal Python program?\n")
print("def proc(x):")
print("    return x + 2\n")
print("def main():")
print("    x = proc(5)")
print("    y = proc(4)\n")
print("main()\n")

def proc(x):
    return x + 2
def main():
    x = proc(5)
    y = proc(4)
    print("Answers: x =", x, "& y =", y)
    
main()

print("\nYes, Even though variable x is used as local variable in main and formal parameter name in function proc, still no conflict as x is used in two distinct quantities.")