#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    char name[10];
    char c;
    int n=4;
    printf("Take Input:\n");
    for(int i =0;i<n;i++)
    {
        scanf("%c",&name[i]);
        scanf("%c",&c);
    }
    name[n] = '\0';
    printf("%s",name);
    return 0;
}