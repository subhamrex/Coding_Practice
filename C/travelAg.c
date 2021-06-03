#include <stdio.h>
//structure define
struct travelAgency
{
    char name[20];
    char dlNo[30];
    char route[20];
    int kms;
};

int main()
{
    //variable declaration
    struct travelAgency driver[4];
    //welcome  message
    printf("\n*****Welcome to our TRAVEL AGENCY please enter your details*****\n\n");
    //store information using loop
    for (int i = 1; i <= 3; i++)
    {
        printf("Enter Driver no %d Name:\n", i);
        fflush(stdin);
        gets(driver[i].name);

        printf("Enter Driver no %d DL no:\n", i);
        scanf("%s", driver[i].dlNo);

        printf("Enter Driver no %d Route\n", i);
        fflush(stdin);
        gets(driver[i].route);

        printf("Enter Driver no %d kms:\n", i);
        scanf("%d", &driver[i].kms);

        printf("\n");
    }
    //printing message
    printf("\n*****Printing Details of Drivers*****\n\n");
    //print using loop
    for (int i = 1; i <= 3; i++)
    {
        printf("Driver no %d Name is:%s\n", i, driver[i].name);

        printf("Driver no %d DL no is:%s\n", i, driver[i].dlNo);

        printf("Driver no %d Route is:%s\n", i, driver[i].route);

        printf("Driver no %d kms is:%d\n", i, driver[i].kms);

        printf("\n");
    }

    return 0;
}