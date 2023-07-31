# Create a Mad Libs program that reads in text files and lets the user add 
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears 
# in the text file. 
from pathlib import Path
import sys
import pyinputplus as pyip

# p = Path('ch09_readingWritingFiles/Quizzes')
p = Path()

# Open a specific file template if there is a user input
# Usage: py madLibs.py <file name>
fileName = 'base.txt'
if len(sys.argv) == 2:
  fileName = sys.argv[1]

# Replace this later on with argv style to access ANY text file
fd = open(p / fileName)
baseContent = fd.readlines()
fd.close()

ctr = 0
print(str(baseContent) + '\n')
for line in baseContent:
  lineSplit = line.split()

  i = 0
  for word in lineSplit:
    # Ask user for input if it is an ADJECTIVE
    if "ADJECTIVE" in word:
      inAdj = pyip.inputStr('Enter an adjective:\n')
      lineSplit[i] = word.replace("ADJECTIVE", inAdj)
    # Ask user for input if it is an NOUN
    elif "NOUN" in word:
      inNoun = pyip.inputStr('Enter a noun:\n')
      lineSplit[i] = word.replace("NOUN", inNoun)
    # Ask user for input if it is an ADVERB
    elif "ADVERB" in word:
      inAdverb = pyip.inputStr('Enter an adverb:\n')
      lineSplit[i] = word.replace("ADVERB", inAdverb)
    # Ask user for input if it is an VERB
    elif "VERB" in word:
      inVerb = pyip.inputStr('Enter a verb:\n')
      lineSplit[i] = word.replace("VERB", inVerb)

    i += 1

  baseContent[ctr] = ' '.join(lineSplit)
  ctr += 1

# print(baseContent)
fw = open(p / 'newFile.txt', 'w')
for line in baseContent:
  fw.write(str(line) + '\n')
fw.close()