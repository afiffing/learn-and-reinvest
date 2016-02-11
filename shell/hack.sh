#!/bin/bash
read num
k=0
for a in $(seq $num); 
do
read new 
k=$(( $k + $new ))
done
printf "%.3f" $(echo "$k/$num" | bc -l)
