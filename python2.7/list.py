#!/bin/python

L=[]

n1=input()
dict=[]

for a in range(0,n1):
	s = raw_input()
	data = s.split(" ")
        print data
	dict.append({'comm':data[0],'v1':data[1]})
        print dict
    	for a in dict:
                if (a['comm']=="append"):
                        L.append(a['v1'])
                elif (a['comm']=="insert"):
                        L.insert(a['v1'],a['v2'])
                elif (a['comm']=="remove"):
                        L.remove(a['v1'])
                elif (a['comm']=="pop"):
                        L.pop(a['v1'])
                elif (a['comm']=="index"):
                        L.index(a['v1'])
                elif (a['comm']=="count"):
                        L.count(a['v1'])
                elif (a['comm']=="sort"):
                        L.sort()
                elif (a['comm']=="reverse"):
                        L.reverse()



