#!/usr/bin/env python
from collections import deque
d=deque()
for x in xrange(input()) :
	m=raw_input().strip().split(' ')
	if m[0]=='append':
		d.append(m[1])
	elif m[0]=='appendleft':
		d.appendleft(m[1])
	elif m[0]=='pop':
		d.pop()
	elif m[0]=='popleft':
		d.popleft()

for _ in d:
	print _,