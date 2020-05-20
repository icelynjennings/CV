#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
		int T;
        scanf("%d", &T);
		
		while (T-- > 0) {
			
			long N;
            scanf("%ld", &N);
			
            long curr_factor;            
			long largest_factor = 1;
            
            /* go through every possible factor of N until sqrt(N) */
			for (curr_factor = 2; pow(curr_factor,2) <= N; curr_factor++) {

				while (N % curr_factor == 0) {
				largest_factor = curr_factor;
				N /= curr_factor;
				}
                
            }

            /* If there are no factors, N is prime */
			if (N > 1) largest_factor = N;
			
			printf("%ld\n",largest_factor);
         }
    return 0;
}