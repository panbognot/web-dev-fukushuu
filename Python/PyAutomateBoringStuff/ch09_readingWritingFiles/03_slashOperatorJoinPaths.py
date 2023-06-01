from pathlib import Path

randomPath = Path('spam') / 'bacon' / 'eggs'
print(randomPath)

# Not safe though as this would only work for windows
homeFolder = str(Path.cwd())
subfolder = 'spam'
fullFolder = homeFolder + '\\' + subfolder
print(fullFolder)

# Use / operator of pathlib to join paths
homeFolder = Path.cwd()
subfolder = Path('bacon')
fullFolder = homeFolder / subfolder
print(fullFolder)