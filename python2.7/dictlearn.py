#!/bin/python
n1=input()

dict = []
for i in range(0,n1):
    s = raw_input()
    data = s.split(" ")
    dict.append({'Name':data[0],'M':data[1],'P':data[2],'C':data[3]})

n2 = raw_input()
for a in dict:
    if (a['Name']==n2):
        print '%.2f' %((float(a['M'])+float(a['P'])+float(a['C']))/3)
