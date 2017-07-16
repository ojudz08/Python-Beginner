print('\nListing 3.6: Temp Conv')
degreesF = eval(input('Enter the temperature in degrees F: '))
degreesC = 5/9*(degreesF - 32)
print(degreesF, 'degrees F =', degreesC, 'degrees C')

print('\nListing 3.7: Time Conv')
seconds = eval(input('Please enter the number of seconds: '))
hours = seconds //  3600 # 3600s in 1 hour
seconds = seconds % 3600
minutes = seconds // 60 # 60s in 1 minute
seconds = seconds % 60
print(hours, 'hr,', minutes, 'min,', seconds, 'sec')

print('\nListing 3.8: Enhanced Time Conv')
seconds = eval(input('Please enter the number of seconds: '))
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60 
seconds = seconds % 60
print(hours, ':', sep="", end="",)
tens = minutes // 10
ones = minutes % 10
print(tens, ones, ':', sep="", end="",)
tens = seconds // 10
ones = seconds % 10
print(tens, ones, sep='')

print('\nListing 3.9: Faulty Temp Conv')
# degreesC should have been after inputing degreesF since degreesF set to 0 at initial
degreesF, degreesC = 0, 0
degreesC = 5/9*(degreesF - 32)
degreesF = eval(input('Enter the temperature in degrees F: '))
print(degreesF, 'degrees F=', degreesC, 'degrees C')
