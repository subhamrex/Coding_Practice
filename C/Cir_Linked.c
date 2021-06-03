#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
};
void C_LinkedLTrav(struct Node *ptr)
 
{ 
     struct Node *ptr1 = ptr;
     do
    {
        printf("Element: %d\n", ptr1->data);
        ptr1 = ptr1->next;
    }while (ptr1 != ptr);
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
    third->next = head;
    C_LinkedLTrav(head);

}