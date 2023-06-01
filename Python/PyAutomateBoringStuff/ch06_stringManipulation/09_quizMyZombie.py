import zombiedice, random

class MyZombie:
  def __init__(self, name, minShotguns=2, riskiness=50):
    # All zombies must have a name:
    self.name = name
    self.minShotguns = minShotguns
    self.riskiness = riskiness

  def turn(self, gameState):
    # gameState is a dict with info about the current state of the game.
    # You can choose t oignore it in your code.

    # diceRollResults = zombiedice.roll() # first roll
    # roll() returns a dictionary with keys 'brains', 'shotgun', and
    # 'footsteps' with how many rolls of each type there were.
    # The 'rolls' key is a list of (color, icon) tuples with the
    # exact roll result information.
    # Example of a roll() return value:
    # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
    #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
    #           ('green', 'shotgun')]}

    # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
    shotguns = 0
    while shotguns < self.minShotguns:
      diceRollResults = zombiedice.roll()

      if diceRollResults is None:
        return

      shotguns += diceRollResults['shotgun']

    # Do a random roll after the minimum shotguns
    if random.randint(0, 100) < self.riskiness:
      diceRollResults = zombiedice.roll()

class AlphaZombie:
  def __init__(self, name, plusLead=0):
    self.name = name
    self.plusLead = plusLead
    self.mainStrategy = zombiedice.examples.MinNumShotgunsThenStopsZombie(name, 2)
    self.altStrategy = zombiedice.examples.MonteCarloZombie(name + '_alt')

  def turn(self, gameState):
    thisZombie = gameState['CURRENT_ZOMBIE']
    highestScoreThatIsntMine = max([zombieScore for zombieName, zombieScore in gameState['SCORES'].items() if zombieName != thisZombie])

    if highestScoreThatIsntMine + self.plusLead > gameState['SCORES'][thisZombie]:
      # If NOT in the lead, do the main strategy
      self.mainStrategy.turn(gameState)
    else:
      # Else, do the alternative strategy
      self.altStrategy.turn(gameState)

zombies = (
  # zombiedice.examples.RandomCoinFlipZombie(name='Random'),
  # zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
  zombiedice.examples.MonteCarloZombie(name='Monte Carlo 50', numExperiments=50),
  zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
  # zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
  # zombiedice.examples.MinNumShotgunsThenStopsOneMoreZombie(name='Stop at 2 Shotguns Plus', minShotguns=2),
  zombiedice.examples.MinNumShotgunsThenStopsOneMoreZombie(name='Stop at 1 Shotgun Plus', minShotguns=1),
  MyZombie(name='My Zombie Bot', riskiness=10),
  AlphaZombie(name='Alpha Zombie', plusLead=10)
  # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)