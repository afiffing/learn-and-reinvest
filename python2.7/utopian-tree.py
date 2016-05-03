#!/usr/bin/env python

#import sys

for a0 in xrange(input()):
    n = int(raw_input().strip())
    if n % 2 == 0:
    	print pow(2,n/2+1)-1
    else:
    	print 2*(pow(2,(n+1)/2)-1)