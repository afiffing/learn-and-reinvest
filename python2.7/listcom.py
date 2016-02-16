#!/usr/bin/env python

x = input()
y = input()
z = input()
n = input()

l1 = [i for i in range(x+1)]
l2 = [i for i in range(y+1)]
l3 = [i for i in range(z+1)]
l4=[]
for i in range(len(l1)):
	for j in range(len(l2)):
		for k in range(len(l3)):
			if (l1[i]+l2[j]+l3[k] != n) :
				l4.append([l1[i],l2[j],l3[k]])

print l4
