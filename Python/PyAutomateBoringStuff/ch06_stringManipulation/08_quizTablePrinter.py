tableData = [['apples', 'oranges', 'cherries', 'banana', 'kiwi'],
             ['Alice', 'Bob', 'Carol', 'David', 'Englats'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
  colNum = len(table)
  colWidths = [0] * colNum
  colItemNums = []

  # Find the length of the longest string per row
  for i in range(colNum):
    colWidths[i] = len(max(table[i], key=len))
    colItemNums.append(len(table[i]))
  
  for i in range(colNum):
    print(colWidths[i], colItemNums[i])

  ctr = 0
  for x in range(colItemNums[ctr]):
    for y in range(colNum):    
      line = table[y][x].rjust(colWidths[y] + 2)
      print(line, end='')
      y += 1
    print()
    ctr += 1

printTable(tableData)