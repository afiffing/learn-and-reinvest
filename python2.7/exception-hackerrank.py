#!/usr/bin/env python
from __future__ import division
for a in xrange(input()):
	try:
		a,b=map(int,raw_input().strip().split(' '))
		print a/b
	except ValueError as ea:
		print "ValueError:",ea
	except ZeroDivisionError as e:
		print "ZeroDivisionError:",e
	