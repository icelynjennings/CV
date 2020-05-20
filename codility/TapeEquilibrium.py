def solution(A):

    # Find all consecutive subarray sums
    sums = []
    
    for k,v in enumerate(A):

        if (k == 0):
            sums.append(v)
            continue

        sums.append(sums[k-1] + v)


    # Find smallest difference between last subarray sum (sum of entire array) and each consecutive subarray
    smallest = 0
    smallest_idx = 0
    
    for k,v in enumerate(sums):

        right_half = sums[-1] - sums[k]
        left_half = v
        
        contender = abs(right_half - left_half)
        contender_idx = k
        
        if (k == 0):
            smallest = contender
            smallest_idx = contender_idx
            continue

        if (k == len(sums) - 1):
            break
        
        if contender < smallest:
            smallest = contender
            smallest_idx = contender_idx
            
    return smallest