#!/bin/python

m = input()
s = raw_input()
n = input()
t = raw_input()

if ((len(s.split(' '))==m) and (len(t.split(' '))==n) ):
	l1 = sorted(map(int,s.split(' ')))
	l2 = sorted(map(int,t.split(' ')))

	set1 = set(l1)
	set2 = set(l2)

	l3=list(set1.difference(set2))
	l4=list(set2.difference(set1))

	for i in l3 :
		print i
	for j in l4 :
		print j
