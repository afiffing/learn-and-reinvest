#!/usr/bin/env python
from collections import OrderedDict
d=OrderedDict()
for i in xrange(input()):
	l=raw_input().strip()
	n =int(l.strip("ABCDEFGHIJKLMNOPQRSTUVWXYZ "))
	m =l.strip("0123456789 ")
	if m not in d.keys():
		d[m]=n
	elif m in d.keys():
		d[m] = n+d.values()[d.keys().index(m)]

for i in xrange(len(d.keys())):
	print d.keys()[i],d.values()[i]