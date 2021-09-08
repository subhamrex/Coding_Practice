
#include <stdio.h>
#include <stdlib.h> 

int MinMaxInTwoArrays(int arr1[], int arr2[], int len1,int len2,int k){

int max= 0;
int min = 0;
int count1 = 0;
int count2 = 0;
for (int i = 0; i < len1; i++)
{
    if(arr1[i] > k){
        max = arr1[i];
        count1++;
    }
}

for (int i = 0; i < len2; i++)
{
    if(arr2[i] < k){
        min = arr2[i];
        count2++;
}


if (count2 < count1){

return count1;

}
else{
    return count2;
}

}
}


int main(int argc, char const *argv[])
{
    int arr1[] = {9,16,12,5,15};
    int arr2[] = {14,7,22,5,32,77};
    int len1 = sizeof(arr1)/sizeof(arr1[0]);
    int len2 = sizeof(arr2)/sizeof(arr2[0]);
    int k = 9;
    int result = MinMaxInTwoArrays(arr1,arr2,len1,len2,k);  
    printf("%d",result);
    return 0;
}
