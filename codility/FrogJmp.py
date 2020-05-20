from __future__ import division
import math

def solution(A, B, step_length):
    distance = B-A
    jumps = math.ceil(distance/step_length)

    return int(jumps)

