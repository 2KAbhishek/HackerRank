#include <stdio.h>

int main()
{
    int num;
    scanf ("%d", &num);
    
    char *strings[] = {"zero","one","two","three","four","five","six","seven","eight","nine"};

    if (num >= 1 && num <= 9){
        printf("%s",strings[num]);
    } else {
        printf("Greater than 9");
    }

    return 0;
}