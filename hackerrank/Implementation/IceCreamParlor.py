t = int(raw_input())

for i in range(t):
    dollars = int(raw_input())
    n = int(raw_input())
    flavors = [int(x) for x in raw_input().split()]

    indexes = []
    numflavors = 0
    for i,v in enumerate(flavors):
        otherflavors = list(flavors)
        otherflavors[i] = -1

        if (dollars-v) > 0 and dollars-v in otherflavors:
            indexes.append(i+1)
            numflavors += 1
            
        if numflavors == 2:
            numflavors = 0
            break
           
    print ' '.join(map(str,indexes))
