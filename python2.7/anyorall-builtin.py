from collections import deque
n,d =input(),deque(raw_input().strip().split(' '))
print all([int(i)>0 for i in d]) and any([i==i[::-1] for i in d])