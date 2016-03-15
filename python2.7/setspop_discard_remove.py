#!/usr/bin/env python

n = int(raw_input().strip())
setsA = set(map(int,raw_input().strip().split(' ')))
N = int(raw_input().strip())

for i in range(N):
	commlist = raw_input().strip().split(' ')
	if len(commlist) == 1 and commlist[0]=='pop':
		setsA.pop()
	elif len(commlist) == 2 :
		if commlist[0] == 'remove':
			setsA.remove(int(commlist[1]))
		elif commlist[0] == 'discard':
			setsA.discard(int(commlist[1]))

print sum(setsA)