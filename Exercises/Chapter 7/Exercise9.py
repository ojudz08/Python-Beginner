print("\nExercise 9. The programmer was expecting the following program to print 200. What does it print instead? Why does it print what it does?\n")
print("def proc(x):")
print("    x = 2*x*x\n")
print("def main():")
print("    num = 10")
print("    proc(num)")
print("    print(num)\n")
print("main()\n")


def proc(x):
    x = 2*x*x
    
def main():
    num = 10
    proc(num)
    print(num)
    
main()

print("\nThe program printed the result 10 as this was initiated equal to 10 on main function. And x variable in proc function was used in two ways, as its local and formal parameter, which have caused conflict.")