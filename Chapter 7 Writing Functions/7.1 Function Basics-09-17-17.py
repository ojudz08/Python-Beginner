print("\nListing 7.1: Simple Function")
print("Creates 'prompt' function asking for an input of integers")
# Print a message to prompt the user for input
def prompt():
    print("\nPlease enter an integer value: ", end="")   
# Start of program
print("\nThis program adds together two integers.")
prompt()        # Call the function
value1 = int(input())
prompt()        # Call the function again
value2 = int(input())
sum = value1 + value2
print(value1, "+", value2, "=", sum)



print("\nListing 7.2: Count to 10")
# Count to ten
for i in range(1, 11):
    print(i)
    
    

print("\nListing 7.3: Count to 10 function")
print("Creates a function counting to ten.")
# Count to ten and print each number on its onw lines
def count_to_10():
    for i in range(1, 11):
        print(i)

print("\nGoing to count to ten . . .")
count_to_10()
print("\nGoing to count to ten again . . .")
count_to_10()



print("\nListing 7.4: Count to n function")
# Count to n and print each number on its own line
def count_to_n(n):
    for i in range(1, n + 1):
        print(i)

print("\nGoing to count to ten . . .")
count_to_n(10)
print("\nGoing to count to five . . .")
count_to_n(5)



print("\nListing 7.4.1: Modified Count to n function")
print("\nModified such that user will input n number to count to n")
# Count to n and print each number on its own line
def count_to_n():
    n = eval(input("\nCount to what number n: "))
    for i in range(1, n + 1):
        print(i)

print("\nGoing to count to n . . .")
count_to_n()
print("\nGoing to count to n again . . .")
count_to_n()



print("\nListing 7.4.2: Modified Count to n function (decreasing)")
print("\nModified such that user will input n number from n to 1")
# From n to 1 and print each number on its own line
def count_to_n():
    n = eval(input("\nCount fom what number n to 1: "))
    for i in range(1, n + 1):
        n -= 1
        print(n+1)

print("\nGoing to count from n to 1 . . .")
count_to_n()
print("\nGoing to count again from n to 1 . . .")
count_to_n()



print("\nListing 7.5: Better prompt")
# Definition of the prompt function
def prompt():
    value = int(input("Please enter an integer value: "))
    return value

print("This program adds together two integers.")
value1 = prompt()       # Call the function
value2 = prompt()       # Call the function again
sum = value1 + value2
print(value1, "+", value2, "=", sum)



print("\nListing 7.6: Even Better prompt")
# Definition of the prompt function
def prompt(n):
    value = int(input("Please enter an integer number: "))
    return value

print("This program adds together two integers.")
value1 = prompt(1)       # Call the function
value2 = prompt(2)       # Call the function again
sum = value1 + value2
print(value1, "+", value2, "=", sum)