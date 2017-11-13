#!/usr/bin/env python



def return_secs(secs):
	if secs == 0:
		return "0 seconds"
	elif secs == 1:
		return "1 second"
	elif secs > 1:
		return str(secs)+" seconds"

def return_time(x):

	mins = divmod(x,60)[0]
	secs = divmod(x,60)[1]

	if mins == 0:
		return return_secs(secs)
	elif mins == 1:
		return "1 minute "+return_secs(secs)
	elif mins > 1:
		return str(mins)+" minutes "+return_secs(secs)

finaltime=[]

for i in range(int(raw_input())):
	rows_col = map(int,raw_input().split(' '))
	virus = raw_input().split(',')
	n = rows_col[0]
	m = rows_col[1]
	r = int(virus[0][1:])
	c = int(virus[1][:-1])
	# took time to figure out that equation, rest was ok.
	time = max([abs(r-1),abs(r-n),abs(c-1),abs(c-m)])
	finaltime.append(return_time(time))

for a in finaltime:
	print a
