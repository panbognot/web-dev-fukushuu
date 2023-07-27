# Create a Mad Libs program that reads in text files and lets the user add 
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears 
# in the text file. 
from pathlib import Path

p = Path('ch09_readingWritingFiles/Quizzes')

# Replace this later on with argv style to access ANY text file
fd = open(p / 'base.txt')
baseContent = fd.readlines()
fd.close()

ctr = 0
for line in baseContent:
  lineSplit = line.split()

  i = 0
  for word in lineSplit:
    # TODO: Ask user for input if it is an ADJECTIVE
    if "ADJECTIVE" in word:
      lineSplit[i] = word.replace("ADJECTIVE", "random adjective")
    # TODO: Ask user for input if it is an NOUN
    elif "NOUN" in word:
      lineSplit[i] = word.replace("NOUN", "random noun")
    # TODO: Ask user for input if it is an ADVERB
    elif "ADVERB" in word:
      lineSplit[i] = word.replace("ADVERB", "random adverb")
    # TODO: Ask user for input if it is an VERB
    elif "VERB" in word:
      lineSplit[i] = word.replace("VERB", "random verb")

    i += 1

  baseContent[ctr] = ' '.join(lineSplit)
  ctr += 1

# print(baseContent)
fw = open(p / 'newFile.txt', 'w')
for line in baseContent:
  fw.write(str(line) + '\n')
fw.close()