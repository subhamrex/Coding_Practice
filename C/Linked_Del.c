#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
};
void LinkedLTrav(struct Node *ptr)
{
    while (ptr != NULL)
    {
        printf("Element: %d\n", ptr->data);
        ptr = ptr->next;
    }
}
struct Node *DelAtFirst(struct Node *head)
{
    struct Node *ptr = head;
    head = head->next;
    free(ptr);
    return head;
}
struct Node *DelAtIndex(struct Node *head, int index)
{
    struct Node *p= head;
    int i = 0;
    while (i != index - 1)
    {
        p = p->next;
        i++;
    }
    struct Node * ptr = p->next; 
    p->next = ptr->next;
    free(ptr);
    return head;
}
struct Node *DelAtEnd(struct Node *head)
{
    struct Node *p = head;
    struct Node *q = head->next;
    
    while (q->next != NULL)
    {
        q = q->next;
        p = p->next;

    }
    p->next = q->next;
    free(q);
    return head;
}
struct Node *DelAtvalue(struct Node *head, int value)
{
    struct Node *p = head;
    struct Node *q = head->next;
    
    while (q->data != value && q->next != NULL)
    {
        q = q->next;
        p = p->next;

    }
    if(q->data == value)
    {
    p->next = q->next;
    free(q);
    }
    return head;
}

int main()
{
    struct Node *head;
    struct Node *first;
    struct Node *second;
    struct Node *third;
    //Allocate heap memory for node
    head = (struct Node *)malloc(sizeof(struct Node));
    first = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));
    //Link the nodes
    head->data = 10;
    head->next = first;
    first->data = 15;
    first->next = second;
    second->data = 20;
    second->next = third;
    third->data = 30;
    third->next = NULL;
    int choice;
    printf("Enter Your choice:\n1.Del at First\n2.Del at Index\n3.Del at Last\n4.Del at value\n");
    scanf("%d", &choice);
    switch (choice)
    {
        case 1:
                head = DelAtFirst(head);
                LinkedLTrav(head);
                break;
        case 2:
                head = DelAtIndex(head,2);   
                LinkedLTrav(head);
                break;  
        case 3:
                head = DelAtEnd(head);    
                LinkedLTrav(head);
                break;
        case 4:
                head = DelAtvalue(head,20);
                LinkedLTrav(head);
                break;

        default:
                printf("Wrong choice!");          

    }

    return 0;
}