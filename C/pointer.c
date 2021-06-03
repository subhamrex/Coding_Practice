#include<stdio.h>
int main()
{
    int arr[]={10,20,30,40};
    int *ptr = arr;
    printf("%d",*(arr+1));
    return 0;
}