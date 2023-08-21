import traceback
from pathlib import Path

p = Path.cwd() / 'ch11_debugging'

try:
  raise Exception('This is the error message.')
except:
  errorFile = open(p / 'errorInfo.txt', 'w')
  errorFile.write(traceback.format_exc())
  errorFile.close()
  print('The traceback info was written to errorInfo.txt.')