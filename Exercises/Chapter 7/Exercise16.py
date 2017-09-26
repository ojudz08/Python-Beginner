print("\nExercise 16. Consider the following function definitions:\n")
print("def fun1(n):")
print("    result = 0")
print("    while n:")
print("        result += n")
print("        n--")
print("    return result\n")
print("def fun2(stars):")
print("    for i in range(stars + 1):")
print('        print(end="*")')
print("    print()\n")
print("def fun3(x, y):")
print("    return 2*x*x* + 3*y\n")
print("def fun4(n):")
print("    return 10 <= n <= 20\n")
print("def fun5(a, b, c):")
print("    return a <= b if b <= c else false\n")
print("def fun6():")
print("    return randrange(0, 1)\n")
print("Examine each of the following statements. If the statement is illegal, explain why it is illegal; otherwise, indicate what statement will print.\n")

def fun2(stars):
    for i in range(stars + 1):
        print(end="*")
    print()

def fun3(x, y):
    return 2*x*x + 3*y

def fun4(n):
    return 10 <= n <= 20

def fun5(a, b, c):
    return a <= b if b <= c else False  # shoudl have been False instead of false
    
print("(a) print(fun1(5))")
print("(b) print(fun1())")
print("(c) print(fun1(5, 2)")
print("Answer: For all a, b and c, since the code n-- is an invalid syntax, fun1 will not work. n-- should have been n +- 1\n")
print("(d) print(fun2(5))")
def maind():
    print(fun2(5))
maind()
print("Answer: The program prints ****** & None\n")
print("(e) fun2(5)")
def maine():
    fun2(5)
maine()
print("Answer: The program prints the same ******\n")
print("(f) fun2(0)")
def mainf():
    fun2(0)
mainf()
print("Answer: The program prints *\n")
print("(g) fun2(-2)")
def maing():
    fun2(-2)
maing()
print("Answer: Nothing\n")
print("(h) print(fun3(5, 2))")
def mainh():
    print(fun3(5, 2))
mainh()
print("Answer: The program prints value 56\n")
print("(i) print(fun3(5.0, 2.0))")
def maini():
    print(fun3(5.0, 2.0))
maini()    
print("Answer: The program prints value 56.0\n")
print("(j) print(fun3('A', 'B'))")
print("Answer: The program does not suport string input.\n")
print("(k) print(fun3(5.0))")
print("Answer: fun3 accpets 2 input\n")
print("(l) print(fun3(5.0, 0.5, 1.2))")    
print("Answer: fun3 accpets 2 input\n")
print("(m) print(fun4(15))")
def mainm():
    print(fun4(15))
mainm()
print("Answer: The program prints True since the input 15 is between 10 and 20\n")
print("(n) print(fun4(5))")
def mainn():
    print(fun4(5))
mainn()
print("Answer: The program prints False since the input 5 is less than 10\n")
print("(o) print(fun4(5000))")
def main0():
    print(fun4(5000))
main0()
print("Answer: The program prints False since the input 5000 is greater than 20\n")
print("(p) print(fun5(2, 4, 6))")
def mainp():
    print(fun5(2, 4, 6))
mainp()
print("Answer: The program prints True since the given satisfies the condition a <= b & b <= c\n")
print("(q) print(fun5(4, 2, 6))")
def mainq():
    print(fun5(4, 2, 6))
mainq()
print("Answer: The program prints False since the given does not satisfies the condition a <= b & b <= c\n")
print("(r) print(fun5(2, 2, 6))")
def mainr():
    print(fun5(2, 2, 6))
mainr()
print("Answer: The program prints True since the given satisfies the condition a <= b & b <= c\n")
print("(s) print(fun5(2, 6))")
print("Answer: No ouptut. The program accepts 3 inputs, given only has 2\n")
print("(t) if fun5(2, 2, 6):")
print('        print("Yes")')
print("    else:")
print('        print("No")')
def maint():
    if fun5(2, 2, 6):
        print("Yes")
    else:
        print("No")
maint()
print("Answer: The program prints Yes as it satisfies the condition a <= b & b <= c\n")
print("(u) print(fun6())")
print("(v) print(fun6(4))")
print("Answer: For u & v, no output as randrange was not defined\n")
print("(w) print(fun3(fun1(3), 3)")
print("(x) print(fun3(3, fun1(3)))")
print("(y) print(fun1(fun1(fun1(3))))")
print("Answer: Since function fun1 has invalid syntax, error will appear for w, x & y\n")
print("(z) print(fun6(fun6()))")
print("Answer: Function fun6 will not work as randrange is not defined.")   