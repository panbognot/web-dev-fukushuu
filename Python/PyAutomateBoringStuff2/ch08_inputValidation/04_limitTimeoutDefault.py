import pyinputplus as pyip

res1 = pyip.inputNum('Enter an integer (2 tries only): ', limit=2)
print(f'Your input is {res1}.')

res2 = pyip.inputNum('Enter an integer (10s only): ', timeout=10)
print(f'Your input is {res2}.')

res3 = pyip.inputNum('Enter an integer', limit=2, default='N/A')
print(f'Your input is {res3}.')