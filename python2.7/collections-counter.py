#!/usr/bin/env python

from collections import Counter
#number of shoes
X = input()
N = map(int,raw_input().strip().split(' '))
p=0
for a in range(input()):
	x = map(int,raw_input().strip().split(' '))
	if x[0] in N:
		p+=x[1]
		N.remove(x[0])
print p