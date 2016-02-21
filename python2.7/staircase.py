#!/usr/bin/env python

n = int(raw_input().strip())
c='#'

for i in range(0,n+1):
	print (c*i).rjust(n,' ')

for i in range(0,n+1):
	print ((n-i)*' ')+ (c*i)
