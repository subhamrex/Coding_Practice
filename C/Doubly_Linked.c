#include<stdio.h>
#include<stdlib.h>
struct Node {
    int data;
    struct Node *prev;
    struct Node *next;
};
void displayForward(struct Node *ptrH) 
{
    struct Node *ptr = ptrH;
    while (ptr!=NULL)
    {   
        printf("Element : %d\n",ptr->data);
        ptr = ptr->next;
    }
      
}
void displayBackward(struct Node *ptrE) 
{   
    struct Node *ptr = ptrE;
    while (ptr!=NULL)
    {   
        printf("Element : %d\n",ptr->data);
        ptr = ptr->prev;
    }
      
}
int main()
{ 
    struct Node *head;
    struct Node *first;
    struct Node *second;
    struct Node *third;
    head = (struct Node *)malloc(sizeof(struct Node));
    first = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));
    //Link nodes
    head->prev = NULL;
    head->next = first;
    first->prev = head;
    first->next = second;
    second->prev = first;
    second->next = third;
    third->prev = second;
    third->next = NULL;
    //Insert value into nodes
    head->data = 20;
    first->data = 25;
    second->data = 30;
    int n3;
    printf("Insert third node data:\n");
    scanf("%d", &n3);
    third->data = n3;
    int choice;
    printf("Enter choice:\n1.Display forward node\n2.Display backward node\n");
    scanf("%d", &choice);
    switch (choice)
    {
        case 1:
                displayForward(head);
                break;
        case 2:
                displayBackward(third);    
                break;
        default:
                printf("Wrong choice!\n");       

    }

    

    
    return 0;
}