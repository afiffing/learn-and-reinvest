#!/usr/bin/env python
from collections import deque
from operator import itemgetter
d=deque()
n,m = map(int,raw_input().strip().split(' '))
for i in xrange(n):
	d.append(tuple(map(int,raw_input().strip().split(' '))))
k=input()
d2 = deque(sorted(d,key=itemgetter(k)))
for i in xrange(n):
	for a in d2[i]: print a,
	print ""