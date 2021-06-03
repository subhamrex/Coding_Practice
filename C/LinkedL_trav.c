#include<stdio.h>
#include<stdlib.h>
struct Node
{
    int data;
    struct Node *next;
};
void LinkedLTrav(struct Node *ptr)
{
    while (ptr!=NULL)
    {
        printf("Element: %d\n",ptr->data); 
        ptr = ptr->next;
    }
}
int main()
{
    struct Node * head;
    struct Node * first;
    struct Node * second;
    struct Node * third;
    //Allocate heap memory for node
    head = (struct Node *) malloc(sizeof(struct Node));
    first = (struct Node *) malloc(sizeof(struct Node));
    second = (struct Node *) malloc(sizeof(struct Node));
    third = (struct Node *) malloc(sizeof(struct Node));
    //Link the nodes
    head->data = 10;
    head->next = first;
    first->data = 15;
    first->next = second;
    second->data = 20;
    second->next = third;
    third->data = 30;
    third->next = NULL;
    LinkedLTrav(head);

    
    return 0;
}