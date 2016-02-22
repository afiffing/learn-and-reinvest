#!/usr/bin/env python

n = int(raw_input().strip())

alpha='abcdefghijklmnopqrstuvwxyz'

for i in range(0,n):
	print ('-'.join(alpha[(n-1)::-1][0:i]+alpha[(n-1)::-1][i]+alpha[(n-1)::-1][0:i][::-1] )).center((4*n-3),'-')

for i in range(n-2,-1,-1):
#for i in reversed(range(0,n-1)) :
	print ('-'.join(alpha[(n-1)::-1][0:i]+alpha[(n-1)::-1][i]+alpha[(n-1)::-1][0:i][::-1] )).center((4*n-3),'-'    )
