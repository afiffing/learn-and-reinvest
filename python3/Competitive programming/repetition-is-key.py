#selection sort example

arr = [8,7,6,1,0,9,2]

#for every i, traverse the arr, j will find out/select a minimum i, if j is smaller than i.
#O(n2)

mini=8

j=7,7<8,mini=7
j=6,6<7,mini=6
j=1,1<6,mini=1
j=0,0<1,mini=0
j=9,9<0,mini=0
j=2,2<0,mini=0

8,0=0,8

arr=[0,7,6,1,8,9,2]
mini=7

j=6,6<7,mini=6
j=1,1<6,mini=1
j=8,8<1
j=9,9<1
j=2,2<1

mini=1

7,1=1,7

arr=[0,1,6,7,8,9,2]

mini=6

j=7,7<6
j=8
j=9
j=2,2<6,mini=2

2,6=6,2

arr=[0,1,2,7,8,9,6]

mini=7
j=8,8<7
j=9
j=6,6<7 mini=6

7,6=6,7 


arr=[0,1,2,6,8,9,7]

mini=8

j=9,
j=7,mini=7

7,8=8,7

arr=[0,1,2,6,7,9,8]

mini=9

j=8,8<9,mini=8
8,9=9,8

arr=[0,1,2,6,7,8,9]

mini=9


