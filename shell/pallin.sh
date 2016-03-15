#!/bin/bash
awk '{
c=0
for (i = 1; i <= int(length($1)/2) ; i++) 
 if (substr($1,i,1)==substr($1,length($1)-i+1,1))
 	c+=1

if (c==int(length($1)/2))
	print $1
}

' check.txt

#hackerrank says length($1) = length($1)+1 , i don't know why

