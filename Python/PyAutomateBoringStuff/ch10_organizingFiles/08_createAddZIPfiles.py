import zipfile
from pathlib import Path

p = Path.cwd() / 'ch10_organizingFiles'

# NOTE: This DOES NOT zip an entire folder structure...
newZip = zipfile.ZipFile(p / 'new.zip', 'w')
newZip.write(p / 'cuties', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()