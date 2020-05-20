#!/bin/python

import sys


n = int(raw_input().strip())
matrix_rows = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    matrix_rows.append(a_temp)

sum_prim = 0
sum_sec = 0
 
# Start from first row, first and last value.
# Keep going down diagonally from both ends.
j = n-1    
for i in xrange(n):
    sum_prim += matrix_rows[i][i]
    sum_sec += matrix_rows[i][j]

    j -= 1

    
print abs(sum_prim - sum_sec)
