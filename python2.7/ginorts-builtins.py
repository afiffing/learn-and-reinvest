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
		elif ord(l[i]) in [48,50,52,54,56]:
			d1["even"].append(l[i])
		print l
		return loopyo(l,i+1)

loopyo(s,0)

def finalsort(list):
		return sorted(list)
final=finalsort(d1["low"])+finalsort(d1["Up"])+finalsort(d1["odd"])+finalsort(d1["even"])

def concate_ans(l,i,ans):
	if i<len(l):
		ans+=l[i]
		return concate_ans(l,i+1,ans)
	else:
		print ans

concate_ans(final,0,"")
