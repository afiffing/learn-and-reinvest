#!/usr/bin/env python
#import fileinput
from collections import deque ,OrderedDict,Counter
d = deque()
for i in xrange(input()):
	d.append(raw_input().strip())

#for line in fileinput.input(['100.txt']):	
d2 = dict(Counter(d).items())
o = OrderedDict.fromkeys(d)
print len(o.keys())
for a in o.keys():
	print d2[a],


