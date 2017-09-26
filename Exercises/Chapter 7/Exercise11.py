print("\nExercise 11. Is the following program legal since the actual parameter has a different name from the fomal parameter (y vs. x)? Why or why not?\n")
print("def proc(x):")
print("    return 2*x*x\n")
print("def main():")
print("    y = 10")
print("    print(proc(y))\n")
print("main()\n")

def proc(x):
    return 2*x*x
    
def main():
    y = 10
    print(proc(y))
    
main()

print("\nYes. Variable y passed onto the function proc whereas variable x is the formal parameter in proc.")