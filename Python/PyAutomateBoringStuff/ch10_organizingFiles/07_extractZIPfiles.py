import zipfile, os
from pathlib import Path

p = Path.cwd() / 'ch10_organizingFiles'

exampleZip = zipfile.ZipFile(p / 'cuties.zip')
exampleZip.extractall(path= p / 'example')

# You can also use the command below to extract a single file
# exampleZip.extract('cuties/spam.txt', p / 'example')

exampleZip.close()