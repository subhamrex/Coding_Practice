#include<stdio.h>
#include<stdlib.h>
int main()
{   int n;
    printf("Enter your Size of Array:\n");
    scanf("%d",&n);
    int *ptr;
    ptr = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
    {   printf("Enter element:\n");
        scanf("%d",&ptr[i]);
    }
    for (int i = 0; i < n; i++)
    {   printf("element at index %d is %d\n",i,ptr[i]);
    }
    
    
    
    return 0;
}