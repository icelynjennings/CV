def solution(A):    
    amounts = {}
    
    for i in A:
        try:
            amounts[i] += 1
        except KeyError:
            amounts[i] = 1
    
    unpaired = None
    
    
    for k,v in amounts.iteritems():
        if v%2 != 0:
            unpaired = k

    return unpaired