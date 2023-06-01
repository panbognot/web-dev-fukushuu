import random
import sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0


def roundWon(numWins):
    print('You win!')
    return numWins + 1


def roundLost(numLosses):
    print('You lost!')
    return numLosses + 1


while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # Quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break  # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        comMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        comMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        comMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == comMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r':
        if comMove == 's':
            wins = roundWon(wins)
        elif comMove == 'p':
            losses = roundLost(losses)
    elif playerMove == 'p':
        if comMove == 'r':
            wins = roundWon(wins)
        elif comMove == 's':
            losses = roundLost(losses)
    elif playerMove == 's':
        if comMove == 'p':
            wins = roundWon(wins)
        elif comMove == 'r':
            losses = roundLost(losses)
