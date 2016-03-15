#!/usr/bin/env python

n1 = int(raw_input().strip())
setf = set(map(int,raw_input().strip().split(' ')))
n2 = int(raw_input().strip())
sete = set(map(int,raw_input().strip().split(' ')))

print len(setf.union(sete))