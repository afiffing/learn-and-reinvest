#!/usr/bin/env python

s = raw_input().strip()
st = raw_input().split(' ')

#print st[0]
#print st[1]

l=list(s)

l[int(st[0])]=st[1]

print ''.join(l)
