#!/usr/bin/env python

n = int(raw_input().strip())

setA = set()

for i in range(n):
	setA.add(raw_input().strip())

print len(setA)