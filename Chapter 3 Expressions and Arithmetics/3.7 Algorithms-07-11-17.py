print('\nListing 3.9: Faulty Temp Conv')
# degreesC should have been after inputing degreesF since degreesF set to 0 at initial
degreesF, degreesC = 0, 0
degreesC = 5/9*(degreesF - 32)
degreesF = eval(input('Enter the temperature in degrees F: '))
print(degreesF, 'degrees F=', degreesC, 'degrees C')
