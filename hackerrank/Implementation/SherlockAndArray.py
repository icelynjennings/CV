t = int(raw_input().strip())
for a_i in xrange(t):
    n = int(raw_input().strip())
    a = [int(i) for i in raw_input().split(' ')]

    if n == 1:
        print "YES"
        continue

    # Keep calculating the sums of consecutive integers in the array, save them in a list
    sums = []
    for i,v in enumerate(a):
        if i == 0:
            sums.append(a[i])
            continue

        sums.append(sums[i-1] + v)
 
    # Calculate the difference on each side by subtracting the sum until a certain point from the sum of the full array.
    match = False
    for i,v in enumerate(a):
        if (sums[i-1]) == (sums[-1] - sums[i]):
            match = True
            break
    if match:
        print "YES"
    else:
        print "NO"        
