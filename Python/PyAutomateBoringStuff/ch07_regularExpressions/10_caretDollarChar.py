import re

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello, world!'))
print(beginsWithHello.search('He said hello.') == None)

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.') == None)

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12   3456790') == None)