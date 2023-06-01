import copy

# spam = ['apples', 'bananas', 'tofu', 'cats']
spam = []

def commaFxn(inList):
  lastIndex = len(inList)
  if lastIndex == 0:
    return ''
  
  completeString = ''
  ctr = 1

  for item in inList:
    if ctr == lastIndex:
      completeString += 'and ' + item
    else:
      completeString += item + ', '
    ctr += 1

  return completeString

print(commaFxn(spam))