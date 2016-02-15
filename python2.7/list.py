#!/bin/python


L=[]

n1=input()

dict={}
for a in range(0,n1):
    s = raw_input()
    data = s.split(' ')   
#    print "data",data	
#    print "L",L
    if (len(data) == 1):
        if ( data[0] == 'print' ):
            print L
        elif (data[0]=='sort'):
            L.sort()
        elif (data[0]=='reverse'):
            L.reverse()
	elif (data[0]=='pop'):
            L.pop()

    elif (len(data) == 2):
        if (data[0]=='append'):
            L.append(int(data[1]))
        elif (data[0]=='remove'):
            L.remove(int(data[1]))
        elif (data[0]=='index'):
            L.index(int(data[1]))
        elif (data[0]=='count'):
            L.count(int(data[1]))

    elif ( len(data) == 3):
        if (data[0]=='insert'):
            L.insert(int(data[1]),int(data[2]))




















#    if (len(data) == 2):
#        dict.update({'comm':data[0],'v1':data[1]})
#    elif ( len(data) == 3):
#        dict.update({'comm':data[0],'v1':data[1],'v2':data[2]})
#    else:
#        dict.update({'comm':data[0]})  

