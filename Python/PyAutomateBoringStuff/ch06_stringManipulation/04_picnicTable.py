def printPicnic(itemsDict, leftWidth, rightWidth):
  print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
  for key, val in itemsDict.items():
    print(key.ljust(leftWidth, '.') + str(val).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)