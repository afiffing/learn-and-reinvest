#!/bin/python

n1 = input()
s=raw_input()
d=s.split(' ')
#for i in range(0,n1):
#	d[i]=int(d[i])


t=map(int,d)
print hash(tuple(t))
