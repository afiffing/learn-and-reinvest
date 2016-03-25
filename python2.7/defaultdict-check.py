#!/usr/bin/env python
from collections import defaultdict

n,m = raw_input().strip().split(' ')
d1=defaultdict(list)
d2=defaultdict(list)
d3=defaultdict(list)
for i in xrange(int(n)):
	d1['A'].append(raw_input().strip())
for j in xrange(int(m)):
	d2['B'].append(raw_input().strip())

for x in d2.values()[0]:
	if x not in d1.values()[0]:
		d3[x].append('-1')
	elif x in d1.values()[0]:
		for z in xrange(len(d1.values()[0])):
			if x == d1.values()[0][z] and z+1 not in d3[x]:
				d3[x].append(z+1)
for j in d2.values()[0]:
	for y in d3[j]: 
		print y ,
	print ""