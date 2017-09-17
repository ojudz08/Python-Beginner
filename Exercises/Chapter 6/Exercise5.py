print("\nExercise 5. Write a guessing game program in which the computer chooses at random an integer in the range 1...10. The user's goal is to guess the number in the least number of tries. For each incorrect guess the user provides, the computer provides feedback whether the user's number is too high or to low.\n\nNOTE: I modified this one from 1-100 to 1-10 as it tooks so long for the user to guess the number. ")
from random import randrange
max_value = 0
while max_value <= 1000:
    guess = eval(input("Guess the random number, from 1 to 10: "))
    value = randrange(1, 11)
    if value != guess:
        print("Oh crap! It's wrong, guess again!")
        continue
    else:
        print("You gussed it right! Guessed number is ", value)
        break