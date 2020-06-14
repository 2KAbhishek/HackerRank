#include <stdio.h>

int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
    char *nums[] = {"zero","one","two","three","four","five","six","seven","eight","nine"};

  	for (int i = a; i <= b; i++){
          if (i >= 1 && i <= 9){
              printf("%s\n",nums[i]);
          } else {
              printf(i%2 == 0 ? "even\n" : "odd\n");
          }
      }
    
    return 0;
}

