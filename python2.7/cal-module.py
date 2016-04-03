#!/usr/bin/env python
from collections import deque
import calendar
d = map(int,raw_input().strip().split(' '))
n = calendar.weekday(d[2],d[0],d[1])
print deque(calendar.day_name)[n].upper()