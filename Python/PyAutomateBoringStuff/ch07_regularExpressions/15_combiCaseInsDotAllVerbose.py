import re

complexRegex1 = re.compile('foo', re.IGNORECASE | re.DOTALL)
complexRegex2 = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)