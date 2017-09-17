print("\nExercise 7. Modified Exercise 5. Guessing the random number from 0 to 10. Report the how many tries and how it took for the user to guess the number.")
from random import randrange
from time import clock
max_value = 1
start_time = clock()
while max_value <= 1000:
    guess = eval(input("Guess the random number, from 1 to 10: "))
    value = randrange(1, 11)
    if value != guess:
        print("Oh crap! It's wrong, guess again!")
        max_value += 1
        continue
    else:
        elapsed = clock() - start_time
        print("It took you ", max_value, "tries and ", round(elapsed, 2), "sec to guess the number ", value)
        break