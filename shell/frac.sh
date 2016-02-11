#!/bin/bash

read n
count=$((2**(6-n)))
#echo $count
y=63
x=100

mid=$(($count/2))
#i=$mid
for a in $(seq $y);
do
 for b in $(seq $x);
 do
 if [ $a -ge $count ] && [ $a -lt $(($count+$mid)) ] ; then 
 for i in $(seq $mid -1 1);
 do
   if [ $b -eq $(($x/2-$i)) ] || [ $b -eq $(($x/2+$i)) ] ; then
     echo $i
   fi
 done
#   else 
#     echo -n "_"  
 elif [ $a -ge $(($count+$mid)) ] && [ $b -eq $(($x/2)) ] ; then
     echo -n "1"  
  else    
     echo -n "_"
 fi
done
#echo -e #"\n"
done
