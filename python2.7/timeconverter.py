#!/usr/bin/python

s = raw_input().strip()
t = map(int,s[:-2].split(':'))
if  s[-2:]=='PM':
	if s[:2]=='12':
		print s[:-2]
	else :
		print str(t[0]+12) + (s[2:-2])
elif s[-2:]=='AM':
	if s[:2]=='12':
		print '0'+str(t[0]-12) +(s[2:-2])
	else :
		print s[:-2] 
