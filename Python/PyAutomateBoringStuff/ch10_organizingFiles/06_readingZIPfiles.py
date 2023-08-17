import zipfile, os
from pathlib import Path

p = Path.cwd() / 'ch10_organizingFiles'

exampleZip = zipfile.ZipFile(p / 'cuties.zip')
exampleZip.namelist()

spamInfo = exampleZip.getinfo('cuties/dogs/dutchShepherd.jpg')
spamInfo.file_size
spamInfo.compress_size
f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!'
exampleZip.close()