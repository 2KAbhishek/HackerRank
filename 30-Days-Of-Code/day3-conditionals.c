#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int N; 
    scanf("%d",&N);
    if (N%2 !=0)
        printf ("Weird\n");
    else if (N%2==0 && N<=5 && N>=2)
        printf ("Not Weird\n");
    else if (N%2==0 && N>=6 && N<=20)
        printf ("Weird\n");
    else if (N > 20)
        printf ("Not Weird\n");
    return 0;
}

