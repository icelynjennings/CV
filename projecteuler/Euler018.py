# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input().strip())

for t_i in xrange(t):
    n = int(raw_input().strip())
    
    # Read the input triangle, convert each line into a list of integers
    triangle_rows = []
    for n_i in xrange(n):
        row = map(int,raw_input().split(' '))
        triangle_rows.append(row)
    
    # Take each number from the second to last row, replace it with the sum of the number and the highest number of the two numbers below it.
    while (len(triangle_rows) > 1):
        last_row = triangle_rows.pop()
        secondtolast_row = triangle_rows.pop()
   
        sums_row = []       
        for idx,val in enumerate(secondtolast_row):
            sums_row.append(val + max(last_row[idx],last_row[idx+1]))
            
        triangle_rows.append(sums_row)
    print triangle_rows[0][0]
