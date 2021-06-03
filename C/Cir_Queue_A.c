#include<stdio.h>
#include<stdlib.h>
struct Cir_queue
{
    int size;
    int front;
    int rear;
    int *arr;
};
void enqueue(struct Cir_queue *q,int value)
{
    if(q->rear+1 % q->size == q->front)
    {
        printf("queue overflow");
    }
    else
    {
        q->rear = (q->rear+1)%q->size;
        q->arr[q->rear] = value;
        printf("Enqueuing elements %d\n",value);

    }
    
}
int  dequeue(struct Cir_queue *q)
{
    int a = -1;
    if(q->front == q->rear)
    {
        printf("Dont have any elements to dequeue\n");
    }
    else
    {
       q->front = (q->front + 1) % q->size;
       a = q->arr[q->front];
       return a;
     }
    
}
void display(struct Cir_queue *q)
{
    for (int i = q->front+1; i <=q->rear; i++)
    {
       printf("%d\n", q->arr[i]);
    }
    
}
int isempty(struct Cir_queue *q)
{
     if(q->front == q->rear)
    {
        printf("Dont have any elements to dequeue\n");
    }
}
int isfull(struct Cir_queue *q)
{
    if(q->front == q->rear)
    {
        printf("No elements to dequeue:\n");
    }
}
int main()
{
    struct Cir_queue *q;
    q->size = 5;
    q->front = q->rear = 0;
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