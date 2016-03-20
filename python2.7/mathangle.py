#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import math
c = int(raw_input().strip())
a = int(raw_input().strip())
b = pow((pow(c,2) + pow(a,2)),0.5)
print str(int(round(math.degrees(math.asin(c/b)))))+"°"
