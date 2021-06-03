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
struct Node *insertAtFirst(struct Node *head, int data)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->next = head;
    ptr->data = data;
    return ptr;
}
struct Node *insertAtIndex(struct Node *head, int data, int index)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    struct Node *p = head;
    int i = 0;
    while (i != index - 1)
    {
        p = p->next;
        i++;
    }
    ptr->data = data;
    ptr->next = p->next;
    p->next = ptr;
    return head;
}
struct Node *insertAtEnd(struct Node *head, int data)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    struct Node *p = head;
    while (p->next != NULL)
    {
        p = p->next;
    }
    ptr->data = data;
    ptr->next = NULL;
    p->next = ptr;
    return head;
}
struct Node *insertAtAfterNode(struct Node *head, struct Node *PNode, int data)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->data = data;
    ptr->next = PNode->next;
    PNode->next = ptr;
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
    int choice,index,data;
    printf("Enter Your choice:\n1.Insert at First\n2.Insert at Index\n3.Insert at Last\n4.Insert atAfterNode\n");
    scanf("%d", &choice);
    switch (choice)
    {
    case 1:
        head = insertAtFirst(head, 25); // update head
        LinkedLTrav(head);
        break;
    case 2:
        printf(" where to insert:  ");
         scanf("%d", &index);
         printf("Insert Data: ");
         scanf("%d", &data);
         head = insertAtIndex(head, data, index);
         LinkedLTrav(head);
         break;
    case 3:
        printf("Insert Data: ");
        scanf("%d", &data);
        head = insertAtEnd(head, data);
        LinkedLTrav(head);
        break;
    case 4:
        head = insertAtAfterNode(head,second,49);
        LinkedLTrav(head);
    default:
        printf("Invalid expression!"); 
    }

    

    return 0;
}