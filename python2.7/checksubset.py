for i in range(int(raw_input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.  
    a = int(raw_input()); A = set(map(int,raw_input().split()))
    b = int(raw_input()); B = set(map(int,raw_input().split()))
    print True if sum(B.intersection(A)) == sum(A) else False