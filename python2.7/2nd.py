#!/usr/bin/env python
import sys
n = input()
l1 = map(int,raw_input().strip().split(' '))

z = max(l1)

while max(l1) == z:
    l1.remove(max(l1))

print max(l1)

#a=l1[0]
#if (n == len(l1))and (n>=2 and n<=10) :
#print int(s.split(' '))
  # here this print won't work because int(< should contain a string not a list>)
