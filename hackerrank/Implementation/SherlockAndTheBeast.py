#!/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    # Fill digits with 5's, keep replacing the last five with 3's starting from the end.
    num_5s = n
    num_3s = 0

    pivot = n - 5 # -1

    while (True):

        if num_5s % 3 == 0 and num_3s % 5 == 0:
            print "{}{}".format("5"*num_5s,"3"*num_3s)
            break
        elif pivot < 0:
            print "-1"
            break

        pivot -= 5
        num_5s -= 5
        num_3s += 5   
