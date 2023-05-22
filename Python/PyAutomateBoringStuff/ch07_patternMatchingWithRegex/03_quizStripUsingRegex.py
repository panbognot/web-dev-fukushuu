import re

def regexStrip(mainString, stripPattern=' '):
  stripLeft = re.compile('^(%s)*' % (stripPattern))
  stripRight = re.compile('(%s)*$' % (stripPattern))

  trimmedLeft = re.sub(stripLeft, "", mainString)
  trimmedBoth = re.sub(stripRight, "", trimmedLeft)
  return trimmedBoth

testData = [
  'Hello World', 'HelloHelloHelloYouHelloDumbasses HelloHelloHelloHello',
  '    Hello World   ', '  Hello  World', 'Hello   World   ',
  '   Hello 235sdf sdf 346#$^@ @#%2 ()   world   ',
  '   2343 sdf89  89kjj $@#% ()((***   sdfs  '
]

for test in testData:
  trimmed = regexStrip(test, 'World')
  print(trimmed)