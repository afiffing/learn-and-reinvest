#!/usr/bin/env python

s = raw_input()
sub = raw_input()
t=0
if len(s)>=1 and len(s)<=200:
	for i in range(0,len(s)-len(sub)+1):
		if s[i:i+len(sub)] == sub :
			t+=1
print t

