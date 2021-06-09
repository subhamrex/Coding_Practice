package Java_Practice;



public class Stack {
    int[] stack = new int[6];
    int top = 0;
    public void push(int data){
        if (top == 5){
            System.out.println("Stack is full");
        }
        else{
            stack[top] = data;
            top++;
        }
        }

    public void show(){
        for(int ele:stack){
            if (ele == 0){
                break;
            }
            System.out.println(ele);
        }
    }
    public int pop(){
        int data;
        top--;
        data = stack[top];
        stack[top] = 0;
        return  data;
    }
    public int peek(){
        int data;
        data = stack[top-1];
        return  data;
    }
    public int size(){
        return top;
    }
    public boolean isEmpty(){
        return top <= 0 ;
    }

}
