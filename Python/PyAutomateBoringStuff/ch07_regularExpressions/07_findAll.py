import re

pnRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo1 = pnRegex.findall('Cell: 415-444-3333 Work: 212-555-0000')
print(mo1)

pnGroupedRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo2 = pnGroupedRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo2)