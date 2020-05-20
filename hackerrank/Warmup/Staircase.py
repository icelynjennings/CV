#!/bin/python

n = int(raw_input().strip())

for i in range(0,n):
    print (" " * (n - (i+1)) ) + ("#" * (i+1))
