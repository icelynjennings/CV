T = int(raw_input())

for t_i in range(T):
    N = int(raw_input())
    
    a = 1
    b = 2
    sum = 0
    
    while (b <= N):
        if b%2 == 0:
            sum += b
        tmp = a
        a = b
        b += tmp
    print sum