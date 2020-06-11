#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char s[1024];
    scanf("%s",s);
    int arr[10] = {0};

    for (int i = 0; i < strlen(s); i++){
        if (s[i] >= '0' && s[i] <= '9'){
            arr[s[i] - '0'] += 1;
        }
    }

    for (int i = 0; i < 10; i++){
        printf("%d ",arr[i]);
    }

    return 0;
}

