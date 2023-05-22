from pathlib import Path

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
  print(Path(r'C:\Users\Rad', filename))

# Sample path creations using the "/" operator to join paths
p1 = Path('spam') / 'bacon' / 'eggs'
print(p1)
p2 = Path('spam') / Path('bacon/eggs')
print(p2)
p3 = Path('spam') / Path('bacon', 'eggs')
print(p3)

homeFolder = Path('C:/Users/Admin')
subFolder = Path('Documents/Programming Studies')
p4 = homeFolder / subFolder
# Notice that these print the same thing
print(p4)
print(str(p4))