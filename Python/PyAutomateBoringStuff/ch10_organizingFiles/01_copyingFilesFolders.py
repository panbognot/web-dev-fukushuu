import shutil, os
from pathlib import Path

p = Path.cwd() / 'ch10_organizingFiles'
shutil.copy(p / 'pets.txt', p / 'test_folder')
shutil.copy(p / 'kuma.txt', p / 'test_folder/cute.txt')