def solution(N):
    # write your code in Python 2.7
    
    binary = bin(N)
    num = int(binary[2:])
    numlen = len(str(num))
    
    # Iterate to find the first gap
    inGap = False
    currGapLen = 0
    maxGapLen = 0
    
    for bit in str(num):
        
        bit = int(bit)
        
        if bit == 1:
            inGap = False
        
        if bit == 0:
            inGap = True
            
        if (inGap):
            currGapLen += 1
        else:
            if currGapLen > maxGapLen:
                maxGapLen = currGapLen
            currGapLen = 0
                
    return maxGapLen
    
    pass

