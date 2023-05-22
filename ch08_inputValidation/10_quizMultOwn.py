import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
  # Pick two random numbers:
  num1 = random.randint(0, 9)
  num2 = random.randint(0, 9)
  prompt = '#%s: %s x %s = ' % (questionNumber + 1, num1, num2)
  retries = 3

  timeout = 8   # seconds time
  timeout_start = time.time()

  # Give the person 3 retries for a valid input
  for retry in range(retries):
    # Exit the loop if it has exceeded the allowed time
    if time.time() > timeout_start + timeout:
      print('Out of time!')
      break

    answer = None
    try:
      answer = int(input(prompt))
    except ValueError:
      print('Invalid input. Try again!')
    else:
      # Exit the loop if it has exceeded the allowed time
      if time.time() > timeout_start + timeout:
        print('Out of time!')
        break

      if answer == num1 * num2:
        print('Correct!')
        correctAnswers += 1
      else:
        print('Incorrect...')
      # Exit the loop once there is a valid input
      break

  time.sleep(1)   # Brief pause to let user see the result.

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))