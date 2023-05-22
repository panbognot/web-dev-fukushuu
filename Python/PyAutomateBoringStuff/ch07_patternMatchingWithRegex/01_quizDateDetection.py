import re

dayRegex = re.compile(r'''(
  (0[1-9]|[12]\d|3[01])          # detect days 1-31 only
  )''', re.VERBOSE)
daysData = ['00','01','5','09','31','32','24','100','030']

print('Test Days:')
for day in daysData:
  mo = dayRegex.search(day)
  if mo != None:
    print(mo.group())
  else:
    print('%s is INVALID' % (day))

monthRegex = re.compile(r'''(
  (0[1-9]|1[0-2])                  # detect months 01-12 only
  )''', re.VERBOSE)
monthsData = ['00','01','5','09','12','13','15','31','230']

print('Test Months:')
for month in monthsData:
  mo = monthRegex.search(month)
  if mo != None:
    print(mo.group())
  else:
    print('%s is INVALID' % (month))

yearRegex = re.compile(r'''(
  ([12]\d{3})                     # detect years 1000-2999 only
  )''', re.VERBOSE)
yearsData = ['100','1000','2000','3000','2500','1500','10000','5000','2021','-1234']

print('Test Years:')
for year in yearsData:
  mo = yearRegex.search(year)
  if mo != None:
    print(mo.group())
  else:
    print('%s is INVALID' % (year))

dateRegex = re.compile(r'''
  (0[1-9]|[12]\d|3[01])          # detect days 1-31 only
  /     
  (0[1-9]|1[0-2])                # detect months 01-12 only
  /
  ([12]\d{3})                    # detect years 1000-2999 only
  ''', re.VERBOSE)
datesData = [
  '31/02/2020', '31/04/2021', '05/18/2023', '1/1/1111', '01/1/1111', '1/01/1111',
  '01/01/1111', '11/11/1111', '33/03/2333', '03/33/2333', '03/03/3000', 
  '20/02/2002', '22/2/2222', '29/02/1900', '30/02/2024', '29/02/2100',
  '30/02/2200', '29/02/2300', '30/02/2400', '29/02/2304', '30/02/2460'
]

print('Test Dates (Regex only):')
for dateVal in datesData:
  mo = dateRegex.search(dateVal)
  if mo != None:
    # print(mo.group())
    day, month, year = mo.groups()
    print('Day: %s, Month: %s, Year: %s' % (day, month, year), end='')

    # Validation for Months [04, 06, 09, 11] with 30 days
    if month == '04' or month == '06' or month == '09' or month == '11':
      if day == '31':
        print(' is INVALID')
      else:
        print()

    # Validation for February [02] (considers leap years)
    elif month == '02':
      if int(day) > 29:
        print(' is INVALID')
      else:
        if int(year) % 400 == 0:
          print()
          continue
        if int(year) % 100 == 0 and int(day) == 29:
          print(' is INVALID')
        elif int(year) % 4 == 0:
          print()
        else:
          print(' is INVALID')
    else:
      print()
  else:
    print('%s is INVALID' % (dateVal))