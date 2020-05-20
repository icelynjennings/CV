def solution(A):
    # write your code in Python 2.7
    
    occurances = {}
    
    smallest = None
    
    for x in A:
        occurances[x] = 1
        

        
    for x in range(0,len(occurances)+1):

        nextint = occurances.get(x+1)
        
        if nextint == None:
            return x+1