print('\nExercise 24. Rewrites the code below')
print('Uses break on the re-written code')
done = False
n, m = 0, 100
while not done and n != m:
    n = eval(input())
    if n < 0:
        done = True
    print("n = ", n)
print("\nHere's the re-written code.", end='')
n, m = 0, 100
while n != m:
    n = eval(input())
    if n > 0:
        done = True
    else:
        break
    print("n = ", n)