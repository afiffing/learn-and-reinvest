#!/usr/bin/env python
import time
import itertools
from collections import Counter, OrderedDict
d=OrderedDict()
start_time = time.time()

#m = [ raw_input().strip() for _ in xrange(input()) ]
#for i in m:
#	d[i]=1
l=[]
for i in xrange(input()):
	m=raw_input().strip()
	l.append(m)
	d[m]=1

print len(d.keys())
for i in d.keys():
	print i



print("--- %s seconds ---" % (time.time() - start_time))

