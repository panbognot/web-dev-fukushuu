import pyinputplus as pyip

res1 = pyip.inputNum('Enter a number: ')
print(f'Your input is {res1}.')

# Input must be minimum of 4
res2 = pyip.inputNum('Enter num: ', min=4)
print(f'Your input is {res2}.')

# Input must be greater than 4
res3 = pyip.inputNum('Enter num: ', greaterThan=4)
print(f'Your input is {res3}')

# Input must be between 4 and 9
res4 = pyip.inputNum('>', min=4, lessThan=10)
print(f'Your input is {res4}')