#!/bin/python
from __future__ import print_function
import sys

n = input()

for a in xrange(1,n+1):
	print(a,sep='',end='',file=sys.stdout)
