print("\nListing 7.13: Tree Function")
#   tree(height)
#      Draws a tree of a given height
#      height is the height of the display tree
def tree(height):
    row = 0                 #  First row, from the top, to draw
    while row < height:     #  Draw one row for every unit of height
        #   Print leading spaces
        count = 0
        while count < height - row:
            print(end=" ")
            count += 1
        #  Print out stars, twice the current row plus one:
        #   1. number of stars on left side of tree
        #      = current row value
        #   2. exactly one star in the center of tree
        #   3. number of stars on right side of tree
        #      = current row value
        count = 0 
        while count < 2*row + 1:
            print(end="*")
            count += 1
        print()             #  Move cursor down to next line
        row += 1            #  Change to the next row

#  main
#     Allows users to draw trees of various heights
def main():
    height = int(input("Enter height of tree: "))
    tree(height)

main ()     #  Runs the program