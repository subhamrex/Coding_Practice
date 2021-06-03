#include <stdio.h>
#include <stdlib.h>
struct Node *front = NULL;
struct Node *rear = NULL;
struct Node
{
    int data;
    struct Node *next;
};
void LinkedLTrav(struct Node *ptr)
{
    printf("Printing Linked List elements:\n");
    while (ptr != NULL)
    {
        printf("Element: %d\n", ptr->data);
        ptr = ptr->next;
    }
}
void enqueue(int value)
{
    struct Node *n = (struct Node *)malloc(sizeof(struct Node));
    if (n == NULL)
    {
        printf("Queue is full!\n");
    }
    else
    {
        n->data = value;
        n->next = NULL;
        if (front == NULL)
        {
            front = rear = n;
        }
        else
        {
            rear->next = n;
            rear = n;
        }
    }
}
int dequeue()
{
    int value = -1;
    struct Node *n = front;
    if (front == NULL)
    {
        printf("Queue is empty\n");
    }
    else
    {
        front = front->next;
        value = n->data;
        free(n);
        return value;
    }
}

int main()
{

    LinkedLTrav(front);
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    printf("Dequeuing element: %d\n", dequeue());
    LinkedLTrav(front);

    return 0;
}