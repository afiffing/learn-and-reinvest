#!/usr/bin/env python

import re
for x in xrange(input()):
    try:
        re.compile(raw_input())
        print True
    except re.error:
    	print False