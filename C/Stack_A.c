#include<stdio.h>
#include<stdlib.h>
struct stack
{
    int size;
    int top;
    int *arr;
};
int  pop(struct stack *ptr)
{
    if(ptr->top == -1)
    {
        printf("Stack is underflow! Cant pop from the stack\n");
    }
    else{
        int val = ptr->arr[ptr->top];
        ptr->top--;
        return val;

    }
}
void push(struct stack *ptr,int value)
{
    if(ptr->top == ptr->size-1)
    {
         printf("Stack is Overflow! Cant push %d to stack\n",value);
    }
    else{
        ptr->top++;
        ptr->arr[ptr->top] = value;
    }
}
int peek(struct stack *ptr,int index)
{
    int arrIndex = ptr->top - index +1;
    if (arrIndex< 0)
    {
        printf("Invalid Index: %d\n",arrIndex);
        return -1;
    }
    else
    {
        return ptr->arr[arrIndex];
        
    }
    
}
int IsEmpty(struct stack *ptr)
{
    if(ptr->top == -1)
    {   
        return 1;
    }
    else
    {
        return 0;
    }
    
    
}
int IsFull(struct stack *ptr)
{
    if(ptr->top == ptr->size-1)
    {
       return 1;
    }
    else
    {
        return 0;
    }
    
    
}
int main()
{   struct stack *s = (struct stack *)malloc(sizeof(struct stack));
    s->size = 5;
    s->top = -1;
    s->arr = (int *)malloc(s->size * sizeof(int));
   
    
    printf("%d\n",IsFull(s));
    printf("%d\n",IsEmpty(s));
    push(s,20);
    push(s,40);
    push(s,50);
    push(s,60);
    push(s,70);
    printf("%d\n",pop(s));
    for (int i = 1; i <= s->top+1; i++)
    {
        printf("Element %d at position %d\n",peek(s,i),i);
    }
    
    
    printf("%d\n",IsFull(s));
    printf("%d\n",IsEmpty(s));
    
   
    

    

    return 0;
}