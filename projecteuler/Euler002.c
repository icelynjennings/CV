#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int T;
    scanf("%d",&T);
    
    while (T--) {
        
        long long N;
        scanf("%lld",&N);
        
        long long sum = 0;
        long long a = 1;
        long long b = 2;
        long long tmp;
        
        while (b <= N) {
            if (b % 2 == 0) sum += b;
            
            tmp = a;
            a = b;
            b += tmp;
        }
        
        printf("%lld\n",sum);
        
    }  
    return 0;
}