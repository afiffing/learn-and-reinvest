#!/usr/bin/env python
from collections import defaultdict

n,m = map(int,raw_input().strip().split(' '))
l=[]
d=defaultdict(list)
for i in xrange(n):
	l.append(raw_input().strip())
for j in xrange(m): 
	k = raw_input().strip()
	if k not in l:
		d[k].append('-1')
	elif k in l:
		for z in xrange(len(l)):
			if l[z]==k and z+1 not in d[k] :
				d[k].append(z+1)
	for z in d[k]:
		print z,
	print ""