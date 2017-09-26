print("\nExercise 12. Complete the following distance function that computes the distance between two geometric points (x1, y1) and (x2, y2):\n")
print("def distance(x1, yx, x2, y2):")
print("    ...")
print("Test it with several points to convince yourself that it is correct.")


from math import sqrt

def dist(x1, y1, x2, y2):
    return sqrt(((x2 - x1)*(x2 - x1))+((y2 - y1)*(y2 - y1)))

def main():
    x1, y1, x2, y2 = eval(input("Enter (x1, y1) and (x2, y2): "))
    print(dist(x1, y1, x2, y2))
    
main()