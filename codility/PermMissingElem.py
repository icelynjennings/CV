def solution(A):
    
    sum_B = 0
    sum_A = 0
        
    for x in xrange(len(A)):
        sum_A += A[x]
        sum_B += x + 1

    sum_B += len(A)
    
    return sum_B - sum_A + 1