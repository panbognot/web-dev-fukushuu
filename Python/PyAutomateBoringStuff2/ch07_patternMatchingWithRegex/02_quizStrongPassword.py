from operator import le
import re

upperLowerCaseRegex = re.compile(r'''(
  .*[a-z]+.*[A-Z]+.*\d+.*|
  .*[A-Z]+.*[a-z]+.*\d+.*|
  .*\d+.*[A-Z]+.*[a-z]+.*|
  .*\d+.*[a-z]+.*[A-Z]+.*|
  .*[a-z]+.*\d+.*[A-Z]+.*|
  .*[A-Z]+.*\d+.*[a-z]+.*
  )+''', re.VERBOSE)

passwords = [
  'akoito', 'akosiminokawa', 'Akosiminokawa', 'Akosiminokawa23',
  'JeJeMoNStyle', 'jEjE12', 'jEjE1234', 's7Q35ksd9', 'q223iQ32ss',
  'this352LooksRandom', 'pogilangnamanako', 'GAGOKALANG',
  'BaklaSiMackieNgSenslope2013' 
]

for pwd in passwords:
  if len(pwd) < 8:
    print('%s is weak...' % (pwd))
  else:
    mo = upperLowerCaseRegex.search(pwd)
    if mo != None:
      print('%s is STRONG!!!' % (mo.group()))
    else:
      print('%s is weak...' % (pwd))