#include <cstdio>
#include <cstdlib>

int main(){
    int n; 
    scanf("%d",&n);
    int sum = 0;
    int x;
    for(int arr_i = 0; arr_i < n; arr_i++){

       scanf("%d",&x);
       sum += x;
    }
    printf("%d",sum);
    return 0;
}