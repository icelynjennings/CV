# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for i in xrange(t):
    n = int(raw_input().strip())
    n = n-1 # Find one below n

    # TODO change to functions
    num_of_3s = (n / 3)
    num_of_5s = (n / 5)
    num_of_15s = (n / 15)
    
    last_multiple_3 = num_of_3s * 3
    last_multiple_5 = num_of_5s * 5
    last_multiple_15 = num_of_15s * 15
    
    # Arithmetic series: ( n * (first_num + last_num) ) / 2
    sum_of_3s = (num_of_3s * (3 + last_multiple_3)) / 2
    sum_of_5s = (num_of_5s * (5 + last_multiple_5)) / 2
    sum_of_15s = (num_of_15s * (15 + last_multiple_15)) / 2
    
    print sum_of_3s + sum_of_5s - sum_of_15s
