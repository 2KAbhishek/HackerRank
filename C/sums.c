#include <stdio.h>
int main()
{
    int a, b;
    float m, n;
    scanf("%d %d %f %f", &a, &b, &m, &n);
    printf("%d %d\n", a+b, a-b);
    printf("%.1f %.1f", m+n, m-n);
    return 0;
}

