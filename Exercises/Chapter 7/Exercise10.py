print("\nExercise 10. Is the following program legal since the variable x is used in two different places (proc and main)? Why or why not?\n")
print("def proc(x):")
print("    return 2*x*x\n")
print("def main():")
print("    x = 10")
print("    print(proc(x))\n")
print("main()\n")

def proc(x):
    return 2*x*x
    
def main():
    x = 10
    print(proc(x))
    
main()

print("\nYes. Variable x is used differently in function proc (as formal parameter) and function main (as local variable). Therefore would not result to conflict.")