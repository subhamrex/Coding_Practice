#include<stdio.h>
int add(int *x,int *y){
    return *x + *y;
}
int subs(int *x,int*y){
    return *x -*y;
}
int main()
{
    int a =10,b=5;
    printf("Addition of %d and %d is %d\n",a,b,add(&a,&b));
    printf("Substraction of %d and %d is %d\n",a,b,subs(&a,&b));
    return 0;
}