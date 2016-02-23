#!/usr/bin/env python
import sys

i3=0
i5=0

t = int(raw_input().strip())
for a0 in xrange(t):
	n = int(raw_input().strip())
	if n == 1 :
		print '-1'
	elif n>1  :
 		
	for i in s:
		print i
		if i=='3' or i=='5':
			if i=='3':
				i3=i3+1
			elif i=='5':
				i5=i5+1
	
print i3%5,i5%3
