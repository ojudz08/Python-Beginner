print("\nExercise 6. Modified Exercise 5. Guessing the random number from 0 to 10. Report the how many tries the user guessed the number.")
from random import randrange
max_value = 1
while max_value <= 1000:
    guess = eval(input("Guess the random number, from 1 to 10: "))
    value = randrange(1, 11)
    if value != guess:
        print("Oh crap! It's wrong, guess again!")
        max_value += 1
        continue
    else:
        print("It took you", max_value, "tries to guess the number ", value)
        break