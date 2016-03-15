#!/bin/bash

awk '{
if (NR==1)
	a=$1
	for(i=2;i<=a+1;i++)
		if (i==NR) 
			f=$1 ;
			c=1 ;
			for (j=f;j>=1;j--) c=c*j;
			print c;
}' check.txt2 | sed 1d