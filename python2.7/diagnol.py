#!/usr/bin/env python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

print a
k1=0
k2=0
for i in range(0,n):  
	k1 = k1 + a[i][n-(n-i)]
	k2 = k2 + a[n-(n-i)][n-i-1]

print abs(k1-k2)

