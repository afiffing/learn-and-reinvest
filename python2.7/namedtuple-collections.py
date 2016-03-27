#!/usr/bin/env python
from __future__ import division
from collections import namedtuple
n = input()
l = []
c=0
section = namedtuple('section',raw_input().strip())
for k in xrange(n):
	l = raw_input().strip().split()
	if 'MARKS' in  section._fields:
		c+=int(l[section._fields.index('MARKS')])
print "%.2f" % float(c/n)		