#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

/* return the sum of all multiples of M below N */
long long sum_multiples(long M, long N) {
    
    long long number_of_multiples = (N / M);
    long long highest_multiple = M * number_of_multiples;
    long long result = (number_of_multiples * (M + highest_multiple)) / 2 ;
    return result;
    
}

int main() {

    int T;
    scanf("%d",&T);
    while (T--) {
        long long N;

        scanf("%lld",&N);
        N -= 1;
        printf("%lld\n", sum_multiples(3,N) + sum_multiples(5,N) - sum_multiples(15,N));
        
    }
    return 0;
}
