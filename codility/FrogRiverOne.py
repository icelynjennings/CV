def solution(num_positions, seconds):
        
    covered = {}
        
    # Find possible results
    for i,v in enumerate(seconds):
        covered[v] = 1
        
        if len(covered) == num_positions:
            return i
            
    # Result not found
    return -1