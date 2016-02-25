#!/usr/bin/env python

from __future__ import division
n = int(raw_input().strip())
set1 = set(map(int,raw_input().strip().split(' ')))

print  float(sum(set1)/len(set1))