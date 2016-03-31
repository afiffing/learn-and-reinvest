#!/usr/bin/env python
from collections import deque
for x in xrange(input()) :
	s=0
	n=input()
	d = deque(raw_input().strip().split())
	while s==0:
		if d[0]>d[-1] or d[0]==d[-1]:
			s = d[0]
			d.popleft()
		elif d[-1]>d[0]:
			s = d[-1]
			d.pop()
	while len(d)>0 :
		if s>=d[0] and d[0]>=d[-1]:
			s = d[0]
			d.popleft()
		elif s>=d[-1] and d[-1]>=d[0]:
			s = d[-1]
			d.pop()
		else:
			break

	if len(d)==0:print "Yes"
	else:print "No"