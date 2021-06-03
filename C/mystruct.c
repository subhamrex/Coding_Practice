#include <stdio.h>
#include<string.h>
struct EmpDetails
{
    int id;
    char name[50];
    int age;
} e1, e2;
int main()
{
    e1.id = 10;
    e2.id = 11;
    strcpy(e1.name,"Subham");
    strcpy(e2.name,"Adi");
    e1.age = 24;
    e2.age = 23;
    printf("%d\n",e1.id);
    printf("%s",e1.name);

    return 0;
}