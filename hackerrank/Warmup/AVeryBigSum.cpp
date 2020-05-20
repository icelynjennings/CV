#include <cstdio>
#include <cstdlib>


int main(){
    int n; 
    scanf("%d",&n);
    long sum;
    
    long x;
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%ld",&x);
       sum += x;
    }
    printf("%ld",sum);
    return 0;
}
