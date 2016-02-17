#!/usr/bin/env python
from operator import itemgetter
n = input()
name = []
k = []
final =[]
if n>=2 and n<=5:
	for i in range(0,n):
		name.append([raw_input().split()[0],map(float,raw_input().split())[0]]
)
	
for a in range(0,n):
       	k.append(sorted(name,key=itemgetter(1))[a][1])

z=min(k)
while min(k) == z:
    k.remove(min(k))

for b in range (0,n):
	if min(k) == sorted(name,key=itemgetter(1))[b][1] :
		 final.append(sorted(name,key=itemgetter(1))[b][0])

for c in sorted(final) :
	print c
