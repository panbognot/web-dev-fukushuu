import re

# Create regular expression to detect dates in the format
# of DD/MM/YYYY.
# Days range from 01 to 31
# Months range from 01 to 12
# Years range from 1000 to 2999

dateRegex = re.compile(r'''(
    (0[1-9]|[12][0-9]|3[01])     # Days from 01 to 31
  )''', re.VERBOSE)

testDays = ['01', '9', '15', '29', '31', '35', '-12', '100']
for day in testDays:
  mo = dateRegex.search(day)
  if mo != None:
    print('%s is OK.' % (mo.group()))
  else:
    print('%s is Invalid.' % (day))

monthRegex = re.compile(r'''(
    (0[1-9]|1[0-2])              # Month from 01 to 12
  )''', re.VERBOSE)

testMonths = ['00', '3', '08', '10', '12', '15', '34']
for month in testMonths:
  mo = monthRegex.search(month)
  if mo != None:
    print('%s is OK.' % (mo.group()))
  else:
    print('%s is Invalid.' % (month))

yearRegex = re.compile(r'''(
    ([12]\d{3})                  # Years from 1000 to 2999
  )''', re.VERBOSE)

testYears = ['00', '1233', '1999', '2500', '3000', '0001', '5358']
for year in testYears:
  mo = yearRegex.search(year)
  if mo != None:
    print('%s is OK.' % (mo.group()))
  else:
    print('%s is Invalid.' % (year))

testDates = ['31/02/2020', '31/04/2021', '27/07/1988', '12/12/0999', '13/13/2013', '31/31/2222']
dateRegex = re.compile()