#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n;
    //calloc
    printf("Enter your Size of Array:\n");
    scanf("%d", &n);
    int *ptr;
    ptr = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++)
    {
        printf("Enter element:\n");
        scanf("%d", &ptr[i]);
    }
    for (int i = 0; i < n; i++)
    {
        printf("element at index %d is %d\n", i, ptr[i]);
    }

    //realloc
     printf("Enter your new Size of Array:\n");
    scanf("%d",&n);
    ptr = (int*)realloc(ptr,n*sizeof(int));
    for (int i = 0; i < n; i++)
    {   printf("Enter new element:\n");
        scanf("%d",&ptr[i]);
    }
    for (int i = 0; i < n; i++)
    {   printf(" New element at index %d is %d\n",i,ptr[i]);
    }

    return 0;
}