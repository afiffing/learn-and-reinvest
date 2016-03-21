#!/usr/bin/env python
from __future__ import division
from itertools import combinations

n = input()
s = raw_input().strip().split(' ')
k = input()
b = sorted(s)
c =0
t =0
for i in list(combinations(''.join(b),k)):
	t +=1
	if 'a' in i:
		c+=1
		
print "%.4f" % (c/t)