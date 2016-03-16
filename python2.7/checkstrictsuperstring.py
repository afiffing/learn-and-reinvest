#!/usr/bin/env python

A = set(map(int,raw_input().strip().split(' ')))
c = True
for i in range(int(raw_input())):
	set1=set(map(int,raw_input().strip().split(' ')))
	if sum(A.intersection(set1)) == sum(set1) and len(A)>len(set1) :
		c = c and True
	else :
		c = c and False
print c