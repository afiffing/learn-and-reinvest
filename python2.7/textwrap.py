#!/usr/bin/python
import textwrap

s = raw_input()
w = int(raw_input())

if len(s)>0 and len(s)<100:
	if w>0 and w<len(s):
		print textwrap.fill(s,w) 

