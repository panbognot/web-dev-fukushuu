import shutil
from pathlib import Path

p = Path.cwd() / 'ch10_organizingFiles'

# Move the file while retaining its filename
shutil.move(p / 'test_folder/pets.txt', p / 'bkp_folder')
# Move the file and rename it
shutil.move(p / 'test_folder/cute.txt', p / 'bkp_folder/kuma.txt')