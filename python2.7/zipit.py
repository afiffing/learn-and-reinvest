#!/usr/bin/env python
from collections import deque
d=deque()
n,x = map(int,raw_input().strip().split(' '))
for i in xrange(x):
	d.append(raw_input().strip().split(' '))
for j in xrange(n):
	print "%.1f" %(sum(map(float,zip(*d)[j]))/x)