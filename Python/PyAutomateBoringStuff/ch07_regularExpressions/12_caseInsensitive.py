import re

robocop = re.compile(r'robocop', re.I)

mo1 = robocop.search('RoboCop is part ma, part machine, all cop.')
print(mo1.group())

mo2 = robocop.search('ROBOCOP protects the innoncent.')
print(mo2.group())

mo3 = robocop.search('Al, why does your programming book talk about robocop so much?')
print(mo3.group())