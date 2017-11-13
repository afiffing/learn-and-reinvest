#!/usr/bin/env python



def merge_the_tools(string, k):
    # your code goes here
   for x in [string[a:a+k] for a in range(0,len(string),k) ]:
   	z = []
   	for y in x:
   		if y not in z:
   			z.append(y)
   	print "".join(z)



if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)


 