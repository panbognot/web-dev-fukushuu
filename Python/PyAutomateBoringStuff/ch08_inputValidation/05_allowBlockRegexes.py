import pyinputplus as pyip

res1 = pyip.inputNum('Enter a Roman Numeral: ', \
    allowRegexes=[r'((I|V|X|L|C|D|M)|(i|v|x|l|c|d|m))+', r'zero'])
print(f'Your input is: {res1}')

res2 = pyip.inputNum('Enter an odd number: ', blockRegexes=[r'[02468]$'])
print(f'Your input is {res2}')

res3 = pyip.inputStr('Enter a string: ', \
    allowRegexes=[r'caterpillar', r'category'], blockRegexes=[r'cat'])
print(f'Your input is {res3}')