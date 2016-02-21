#!/bin/usr/env python
from __future__ import division

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

p=0
n1=0
z=0

for i in a:
	if i>0 :
		p=p+1
	elif i<0 :
		n1=n1+1
	elif i==0 :
		z=z+1
print '%.6f' % float(p/n)
print '%.6f' % float(n1/n)
print '%.6f' % float(z/n)
