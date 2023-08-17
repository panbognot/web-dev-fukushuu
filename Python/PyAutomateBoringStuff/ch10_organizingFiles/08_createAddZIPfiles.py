import zipfile
from pathlib import Path

p = Path.cwd() / 'ch10_organizingFiles'

newZip = zipfile.ZipFile(p / 'new.zip', 'w')
newZip.write(p / 'cuties', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()