#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    
    threshold = k
    student_arrivals = a

    good_students = 0
    for time in student_arrivals:
        if time <= 0:
            good_students += 1

    if good_students < threshold:
        print "YES"
    else:
        print "NO"
