#include <stdio.h>

void calculate_the_maximum(int n, int k) {
    int bigAnd = 0, bigOr = 0, bigXor = 0;
    for (int i = 1; i <= n; i++){
        for (int j = i+1; j <= n; j++){
            int temp;
            temp = i&j;
            if (temp > bigAnd && temp < k) bigAnd = temp;
            temp = i|j;
            if (temp > bigOr && temp < k) bigOr = temp;
            temp = i^j;
            if (temp > bigXor && temp < k) bigXor = temp;
        }
    }
    printf("%d\n%d\n%d", bigAnd, bigOr, bigXor);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
