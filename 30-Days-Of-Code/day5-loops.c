#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int i=1,m,n; 
    scanf("%d",&n);
    while (i<=10)
    {
        m=n*i;
        printf ("%d x %d = %d\n",n,i,m);
        i++;
    }
    return 0;
}

