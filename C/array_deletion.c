#include<stdio.h>
void create_array(int arr[],int n)
{
    for (int i = 0; i < n; i++)
    {   printf("At index %d element is: \n",i);
        scanf("%d",&arr[i]);
    }
    
}
void display(int arr[],int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", arr[i]);
    }
    printf("\n");
    
}
 int deletion(int arr[], int size,int index)
 {
     
     if(index>=size)
     {
         printf("Invalid Index\n");
         return -1;       
     }
     for (int i = index; i < size-1; i++)
     {
         arr[i] = arr[i+1];
     }
     
     return 1;
 }

int main()

{   int capacity,n,index;
    printf("Enter your Array capacity:\n");
    scanf("%d",&capacity);
    int arr[capacity];
    printf("Enter no of element you want :\n");
    scanf("%d",&n);
    create_array(arr,n);
    printf("Array elements:\n");
    display(arr,n);
    printf("Enter your index to delete element:\n");
    scanf("%d",&index);
    deletion(arr,n,index);
    n--;
    display(arr,n);
    return 0;
}