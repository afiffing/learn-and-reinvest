#!/usr/bin/env python

n = map(int,raw_input().strip().split(' '))

arr = map(int,raw_input().strip().split(' '))

def Sets():
	l = map(int,raw_input().strip().split(' '))
	return set(l)
def happiness(xset):
	H=0
	for i in arr:
		if i in xset:
			H += 1
	return H	

print happiness(Sets())-happiness(Sets())
