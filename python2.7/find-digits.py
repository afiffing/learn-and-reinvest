#!/usr/bin/env python

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    c=0
    for i in map(int,str(n)):
    	try:
    		if n%i ==0:
    			c+=1
    	except ZeroDivisionError:
    		pass	
    print c