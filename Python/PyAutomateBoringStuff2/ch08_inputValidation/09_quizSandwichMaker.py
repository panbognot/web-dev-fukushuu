import pyinputplus as pyip

breadPrompt = 'What bread would you like?\n'
proteinPrompt = 'What protein would you like?\n'
cheesePrompt = 'Would you like it with cheese?\n'
cheeseTypePrompt = 'What cheese would you like?\n'
condimentsPrompt = 'Would you like it with mayo, mustard, lettuce and tomato?\n'
numSandwichesPrompt = 'How many sandwiches would you like?\n'

breadTypes = ['wheat', 'white', 'sourdough']
proteinTypes = ['chicken', 'turkey', 'ham', 'tofu']
cheeseTypes = ['cheddar', 'Swiss', 'mozzarella']

sandwich = {
  'bread': None,
  'protein': None,
  'cheese': None,
  'condiments': None
}

order = {
  'sandwich': sandwich,
  'numSandwiches': None,
  'totalPrice': 0
}

priceList = {
  'wheat': 0.6,
  'white': 0.5,
  'sourdough': 0.7,
  'chicken': 2,
  'turkey': 2.5,
  'ham': 2.3,
  'tofu': 1.5,
  'cheddar': 0.3,
  'Swiss': 1,
  'mozzarella': 0.8,
  'yes': 0.2
}

order['sandwich']['bread'] = pyip.inputMenu(choices=breadTypes, 
                                            prompt=breadPrompt,
                                            lettered=True)
order['sandwich']['protein'] = pyip.inputMenu(choices=proteinTypes, 
                                              prompt=proteinPrompt,
                                              lettered=True)
withCheeseRes = pyip.inputYesNo(cheesePrompt)

if withCheeseRes == 'yes':
  order['sandwich']['cheese'] = pyip.inputMenu(choices=cheeseTypes, 
                                              prompt=cheeseTypePrompt, 
                                              lettered=True)

order['sandwich']['condiments'] = pyip.inputYesNo(condimentsPrompt)
order['numSandwiches'] = pyip.inputInt(prompt=numSandwichesPrompt, min=1)

for part, val in order['sandwich'].items():
  if val and val != 'no':
    order['totalPrice'] += priceList[val]

order['totalPrice'] *= order['numSandwiches']

print(order)