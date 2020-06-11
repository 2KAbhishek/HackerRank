#include <stdio.h>

int main(){
    int i,length;
    scanf("%d",&length);
    int arr[length];
    for (i=0;i<length;i++){
    scanf("%d",&arr[i]);    
    }
    for (i=length-1;i>=0;i--){
    printf("%d ",arr[i]);    
    }
}
