#include <stdio.h>
#define MAX(a, b) (( a > b) ? a : b )

int max_of_four(int a, int b, int c, int d){
    return MAX(MAX(a,b), MAX(c,d));
}


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    return 0;
}

