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
 int insertion(int arr[], int size , int capacity,int index,int element)
 {
     if(size>= capacity)
     {   printf("Insertion failed\n");
         return -1;
     }
     if(index>=capacity)
     {
         printf("Invalid Index\n");
         return 0;
     }
     for (int i = size-1; i >= index; i--)
     {
         arr[i+1] = arr[i];
     }
     arr[index] = element;
     return 1;
 }

int main()

{   int capacity,n,index,element;
    printf("Enter your Array capacity:\n");
    scanf("%d",&capacity);
    int arr[capacity];
    printf("Enter no of element you want :\n");
    scanf("%d",&n);
    create_array(arr,n);
    printf("Array elements:\n");
    display(arr,n);
    printf("Enter your preferred index for insertion:\n");
    scanf("%d",&index);
    printf("Enter your element at index %d for insertion:\n",index);
    scanf("%d",&element);
    insertion(arr,n,capacity,index,element);
    n++;
    display(arr,n);

    
    return 0;
}