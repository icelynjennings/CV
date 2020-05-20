#!/bin/python

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

positives = 0.0
negatives = 0.0
zeroes = 0.0

for i in arr:
    if i > 0:
        positives += 1
    elif i < 0:
        negatives += 1
    else:
        zeroes += 1
        
print positives/n
print negatives/n
print zeroes/n
