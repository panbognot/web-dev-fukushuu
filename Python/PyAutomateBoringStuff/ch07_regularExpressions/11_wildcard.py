import re

atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo1)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo2 = nameRegex.search('First Name: Rad Last Name: Navs')
print(mo2.group(1), mo2.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo3 = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo3.group())

greedyRegex = re.compile(r'<.*>')
mo4 = greedyRegex.search('<To serve man> for dinner.>')
print(mo4.group())

longMsg = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'

noNewlineRegex = re.compile('.*')
mo5 = noNewlineRegex.search(longMsg)
print(mo5.group())
print()

newlineRegex = re.compile('.*', re.DOTALL)
mo6 = newlineRegex.search(longMsg)
print(mo6.group())