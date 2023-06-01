import random
numStreaks = 0
for experimentNum in range(10):
  # Code that creates a list of 100 'heads' or 'tails' values.
  experimentNum = [random.randrange(0, 2, 1) for i in range(10000)]

  # Code that checks if there is a streak of 6 heads or tails in a row.
  # Assumptions on what a "streak" is:
  #   1. Any streak more than 6 is counted as multiple streaks of 6
  #     ex. 7 streak => 2 streaks of 6
  #     ex. 9 streak => 4 streaks of 6
  #   2. There will be a counter if the coin doesn't change value
  #   3. The counter is reset when the coin changes value
  numSameValue = 0
  currentCoinFace = None
  for coin in experimentNum:
    if coin == currentCoinFace:
      numSameValue += 1
    else:
      numSameValue = 0

    if numSameValue >= 6:
      numStreaks += 1

    currentCoinFace = coin

print('Chance of streak: %s%%' % (numStreaks / 100))