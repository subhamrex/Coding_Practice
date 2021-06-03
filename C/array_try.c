#include<stdio.h>
#include<stdlib.h>
int mem_al(int t)
{
    return t;
}
int main()
 
{   int t;
    scanf("%d",&t);
    int arr1[t];
    int arr2[50];
    printf("%d",sizeof(arr1)/sizeof(int));
    return 0;
}