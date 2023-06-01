import re

namesRegex = re.compile(r'Agent \w+')
mo1 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo1)

longMsg = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bod was a double agent.'
agentsRegex = re.compile(r'Agent (\w{2})\w*')
mo2 = agentsRegex.sub(r'\1****', longMsg)
print(mo2)