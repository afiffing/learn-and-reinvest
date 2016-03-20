#!/usr/bin/env python
import cmath
z = complex(raw_input().strip())
print '%.3f' % cmath.polar(z)[0]
print '%.3f' % cmath.polar(z)[1]