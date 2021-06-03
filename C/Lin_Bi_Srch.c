#include <stdio.h>
void Linear_srch(int arr[], int n, int ele)
{
    int flag = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == ele)
        {
            printf("Element %d found at index %d\n", ele, i);
            flag = 1;
            break;
        }
    }
    if (flag == 0)
    {
        printf("Not found");
    }
}

void Binary_srch(int arr[], int n, int ele)
{
    int low, mid, high, flag = 0;
    low = 0;
    high = n - 1;
    while (low <= high)
    {

        mid = (low + high) / 2;
        if (arr[mid] == ele)
        {
            printf("Element %d found at index %d\n ", ele, mid);
            flag = 1;
            break;
        }
        else if (arr[mid] < arr[high])
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    if (flag == 0)
    {
        printf("Not found");
    }
}
int main()
{
    int arr[50], n, ele, press;
    printf("Enter No of element you want to add in array:\n");
    scanf("%d", &n);
    printf("Enter Array Elements:\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", arr[i]);
    }
    printf("\n Enter Your Elemenyt You want to find:\n");
    scanf("%d", &ele);
    printf("Which type of search you want to perform:\n Press 1 for Linear search & Press 2 for Binary search\n");
    scanf("%d", &press);
    if (press == 1)
    {
        Linear_srch(arr, n, ele);
    }
    else if (press == 2)
    {
        Binary_srch(arr, n, ele);
    }
    else
    {
        printf("Invalid option!");
    }

    return 0;
}