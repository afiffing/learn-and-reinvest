#!/usr/bin/env python
from collections import defaultdict,OrderedDict
s=raw_input()
d1=defaultdict(list)
def loopyo(l,i):
	if i<len(l):
		if ord(l[i])>=97 and ord(l[i])<=122:
			d1["low"].append(l[i])
		elif ord(l[i])>=65 and ord(l[i])<=90:
			d1["Up"].append(l[i])
		elif ord(l[i]) in [49,51,53,55,57]:
			d1["odd"].append(l[i])
		elif ord(l[i]) in [50,52,54,56]:
			d1["even"].append(l[i])
		return loopyo(l,i+1)
loopyo(s,0)

def sort_withoutloop(l,i):
	if i<len(l) and i!=len(l)-1:
		if l[i]>l[i+1]:
			b=l[i+1]
			l[i+1]=l[i]
			l[i]=b
		return sort_withoutloop(l,i+1)
	else:
		return l

def finalsort(l,i):
	if i < len(l):
		sort_withoutloop(l,0)
		return finalsort(l,i+1)
	else:
		return l

final=finalsort(d1["low"],0)+finalsort(d1["Up"],0)+finalsort(d1["odd"],0)+finalsort(d1["even"],0)

def concate_ans(l,i,ans):
	if i<len(l):
		ans+=l[i]
		return concate_ans(l,i+1,ans)
	else:
		print ans
concate_ans(final,0,"")
