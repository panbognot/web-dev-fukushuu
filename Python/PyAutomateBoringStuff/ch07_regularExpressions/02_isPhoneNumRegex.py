import re

# Beginner's usage
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# More efficient use of regex
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())
