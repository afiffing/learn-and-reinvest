#!/usr/bin/env python
from collections import Counter
from collections import OrderedDict
yo = Counter(raw_input().strip())

f = sorted(yo.values())
dict1 = OrderedDict(sorted(yo.items()))

for i in xrange(3):
	print dict1.keys()[dict1.values().index(f[-1])] , dict1.pop(dict1.keys()[dict1.values().index(f[-1])])
	f.pop()