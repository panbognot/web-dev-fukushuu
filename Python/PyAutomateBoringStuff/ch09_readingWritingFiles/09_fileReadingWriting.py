from pathlib import Path

p = Path('ch09_readingWritingFiles')
helloPath = p / 'hello.txt'
helloPath.write_text('Hello, world!')
helloPath.read_text()

# READING
# You normally open files using open() which returns a File object
sonnetFile = open(p / 'sonnet29.txt')
# This function can also accept strings (for Windows)
# sonnetFile = open('C:\\Users\\your_home_folder\\sonnet29.txt')
# for MacOS
# sonnetFile = open('/Users/your_home_folder/sonnet29.txt')

# Store the content in a variable
sonnetContent = sonnetFile.read()
print(sonnetContent)

# It seems like it is necessary to open the file again for reading
sonnetFile = open(p / 'sonnet29.txt')
# Separate the four lines with line breaks
print(sonnetFile.readlines())

# WRITING
# This assumes that 'bacon.txt' doesn't exist yet
baconPath = p / 'bacon.txt'

# Overwrite file with "Hi Bacon!"
# Apparently, the text is written only when the file is closed...
baconFile = open(baconPath, 'w')
baconFile.write('Hi Bacon!\n')
baconFile.close()

# Append the file
baconFile = open(baconPath, 'a')
baconFile.write('Bacon is NOT a vegetable.')
baconFile.close()

# Open using the default read mode
# Read and print the file content
baconFile = open(baconPath)
content = baconFile.read()
baconFile.close()
print(content)