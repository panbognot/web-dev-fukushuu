from unicodedata import digit
from urllib import response
import pyinputplus as pyip

def addsUpToTen(numbers):
  numbersList = list(numbers)
  for i, digit in enumerate(numbersList):
    numbersList[i] = int(digit)
  if sum(numbersList) != 10:
    raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
  return int(numbers)   # Return an int form of numbers.

# No parentheses after addsUpToTen since we are passing a function
res1 = pyip.inputCustom(addsUpToTen, prompt='Input a number with a sum of 10: ')
print(f'This is your input: {res1}.')