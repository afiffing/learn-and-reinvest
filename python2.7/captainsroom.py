#!/usr/bin/env python

n = int(raw_input().strip())
l1 = map(int,raw_input().strip().split(' '))
set1 = set(l1)

#there are two solutions via loop and via maths , Maths win obviously because of the complexity of the program.
#solution is correct in both the cases , yet get failed to pretty large number of list elements as input room numbers.

#for i in set1:
#	if l1.count(i) < 2 :
#		print i

#Hence this

print (sum(set1)*n - sum(l1))//(n-1)

