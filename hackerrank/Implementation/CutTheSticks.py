#!/bin/python

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

arr = sorted(arr)

while(True):
    cuts = 0

    if len(arr) == 0:
        break
    else:
        smallest = arr[0]
    
    for i in arr:
        if i < smallest:
            i = smallest
            break  
    tokeep = []
        
    for idx,v in enumerate(arr):
        v -= smallest
        cuts += 1
        if v > 0:
            tokeep.append(v)

    arr = tokeep
    print cuts
        
