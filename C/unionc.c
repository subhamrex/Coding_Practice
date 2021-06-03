#include<stdio.h>
union unionc
{
    int id;
    int marks;
} s1;

int main()
{
    s1.id=10;
    s1.marks=20;
    printf("%d",s1.marks);
    return 0;
}