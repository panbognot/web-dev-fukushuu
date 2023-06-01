userNum = None


def collatz(num):
  if num % 2 == 0:
    result = num // 2
  elif num % 2 == 1:
    result = 3 * num + 1

  print(result)
  return result


def getIntFromUser():
  global userNum
  
  while True:
    try:
      print('Type an integer:')
      userNum = int(input())
      break
    except ValueError:
      print('Error: You must type an integer')


getIntFromUser()

while True:
  if userNum == 1:
    break
  else:
    userNum = collatz(userNum)