#!/usr/bin/env python

l=[10,2,8,3,4,1]

def sort_withoutloop(l,i):
	if i<len(l) and i!=len(l)-1:
		if l[i]>l[i+1]:
			b=l[i+1]
			l[i+1]=l[i]
			l[i]=b
		return sort_withoutloop(l,i+1)
	else:
		return l

def anotherfunction(l,i):
	if i < len(l):
		sort_withoutloop(l,0)
		return anotherfunction(l,i+1)
	else:
		print l

anotherfunction(l,0)