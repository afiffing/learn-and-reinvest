#!/usr/bin/env python

for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((pow(10,i)-1)/9)*i

    #Also it can be easily done by using str with any of the methods used below ,but it was not required for the challenge
    #so have to use sum of gp series formula

    #print ("%s" %(i))*i
    #print i*str(i)
    