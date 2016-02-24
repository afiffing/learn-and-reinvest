#!/usr/bin/env python

#HELL LONG code almost took an entire day of mine , at the end getting timeouts due to multiple loops and iterations
#have to try another approach


s = raw_input().strip()
S =[]
K =[]
for i in s : 
	if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
		if i not in K:
			K.append(i)
	else :
		if i not in S:
			S.append(i)
#print S , K

# counts the occurance of a substring in a string s
def occur(s,sub):
	t=0
	for i in range(0,len(s)-len(sub)+1):
		if s[i:i+len(sub)] == sub :
			t+=1
	return t

#creates words starting for the list
def words(list,string):
	for a in list:
		for i in range(len(string)):
			if string[i]==a:
				for b in range(i+2,len(s)+1):
					if s[i:b] not in list :
						list.append(s[i:b])

	return list

#returns the total count of the words
def count(list):
	total=0
	for i in list:
		total=total+occur(s,i)
	return total

words(S,s)
words(K,s)

if count(S) > count(K):
	print 'Stuart'+' '+str(count(S))
elif count(K) > count(S):
	print 'Kevin'+' '+str(count(K))
elif count(S)==count(K):
	print 'Draw'

