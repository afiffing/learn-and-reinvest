#!/usr/bin/python env

n = int(raw_input().strip())
setsA = set(map(int,raw_input().strip().split(' ')))
n2 = int(raw_input().strip())
for i in range(n2):
	comm = raw_input().strip().split(' ')
	setsB = set(map(int,raw_input().strip().split(' ')))
	if len(setsB)==int(comm[1]):
		if str(comm[0])=='update':
			setsA.update(setsB)
		elif str(comm[0])=='intersection_update':
			setsA.intersection_update(setsB)
		elif str(comm[0])=='difference_update':
			setsA.difference_update(setsB)
		elif str(comm[0])=='symmetric_update':
			setsA.symmetric_update(setsB)
		elif str(comm[0])=='symmetric_difference_update':
			setsA.symmetric_difference_update(setsB)	

print sum(setsA)
