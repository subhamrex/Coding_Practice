#include<stdio.h>
#include<stdlib.h>
struct queue
{
    int size;
    int front;
    int rear;
    int *arr;
};
void enqueue(struct queue *q,int value)
{
    if(q->rear ==q->size -1)
    {
        printf("queue overflow");
    }
    else
    {
        q->rear = q->rear+1;
        q->arr[q->rear] = value;

    }
    
}
int  dequeue(struct queue *q)
{
    int a = -1;
    if(q->front == q->rear)
    {
        printf("No elements to dequeue:\n");
    }
    else
    {
       q->front++;
       a = q->arr[q->front];
       return a;
     }
    
}
void display(struct queue *q)
{
    for (int i = q->front+1; i <=q->rear; i++)
    {
       printf("%d\n", q->arr[i]);
    }
    
}
int main()
{
    struct queue *q;
    q->size = 7;
    q->front = q->rear = -1;
    q->arr = (int *)malloc(q->size*sizeof(int));
    enqueue(q,10);
    enqueue(q,20);
    enqueue(q,30);
    enqueue(q,40);
    printf("dequeuing elements %d\n",dequeue(q));
    printf("dequeuing elements %d\n",dequeue(q));
    printf("Left Elements:\n");
    display(q);
    return 0;
}