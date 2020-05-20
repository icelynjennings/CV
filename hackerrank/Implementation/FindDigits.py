#!/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    digits = str(n)
    answer = 0
    for d in digits:
        if d != "0":
            if n % int(d) == 0:
                answer += 1
            
    print answer         
