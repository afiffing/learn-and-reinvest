#!/usr/bin/env python

s = input()

w = len('{:b}'.format(s))

for i in range(1,s+1):
		print '{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'.format(i,w=w)

