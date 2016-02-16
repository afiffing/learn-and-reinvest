#!/bin/python

m = input()
s = raw_input()
n = input()
t = raw_input()

if ((len(s.split(' '))==m) and (len(t.split(' '))==n) ):
	l1 = map(int,s.split(' '))
	l2 = map(int,t.split(' '))

	set1 = set(l1)
	set2 = set(l2)
	set3 = set1.difference(set2).union(set2.difference(set1))
	l3=sorted(list(set3))
#	l4=sorted(list(set2.difference(set1)))

	for i in l3 :
		print i
#	for j in l4 :
#		print j
