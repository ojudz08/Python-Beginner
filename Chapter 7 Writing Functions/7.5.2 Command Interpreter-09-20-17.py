print("\nListing 7.10: Calculator")
print("\nThis program demonstrates a function in which no information is accpeted or returns no result.")
#     help_screen
#        Displays information about how the program works
#        Accepts no parameters
#        Returns nothing
def help_screen():
    print("Add: Adds two numbers")
    print("Subract: Subtracts two numbers")
    print("Print: Displays the result of the latest operation")
    print("Help: Displays this help screen")
    print("Quit: Exits the program")

#   menu
#      Display a menu
#      Accepts no parameters
#      Returns the string entered by the user.
def menu():    
     #  Display a menu
    return input("Please select any\n= A)dd S)ubtract P)rint H)elp Q)uit = \n")

    
#     main
#        Runs a command loop that allows user to
#        perform simple arithmetic
def main():
    result = 0.0
    done = False;   # Intiially not done
    while not done:
        choice = menu()   # Get user's choice
        
        if choice == "A" or choice == "a":     # Addition
            arg1 = float(input("Enter arg 1: "))
            arg2 = float(input("Enter arg 2: "))
            result = arg1 + arg2
            print(result)
        elif choice == "S" or choice == "s":   # Subtraction
            arg1 = float(input("Enter arg 1: "))
            arg2 = float(input("Enter arg 2: "))
            result = arg1 - arg2
            print(result)
        elif choice == "P" or choice == "p":   # Print
            print(result)
        elif choice == "H" or choice == "h":   # Help
            help_screen()
        elif choice == "Q" or choice == "q":   # Quit
            done = True

main()