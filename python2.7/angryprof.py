#!/usr/bin/env python
n1 = 0
t = int(raw_input().strip())
for a0 in xrange(t):
	n,k = raw_input().strip().split(' ')
	n,k = [int(n),int(k)]
	a = map(int,raw_input().strip().split(' '))
	for i in a:
		if i<=0:
			n1=n1+1
	if k <= n1 :
		print 'NO'
		n1=0
	elif k>n1 :
		print 'YES'
		n1=0
