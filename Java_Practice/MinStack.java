package Java_Practice;

class MinStack {
    int[] stack = new int[10000];
    int[] min = new int[10000];
    int topPtr;
    int minPtr;

    MinStack() {
        topPtr = -1;
        minPtr = -1;
    }

    void push(int x) {
        if(topPtr >= 10000)
            return;

        stack[++topPtr] = x;

        if(minPtr >= 0)
        {
            if(min[minPtr] > x)
                min[++minPtr] = x;
            else
            {
                min[minPtr+1] = min[minPtr];
                minPtr += 1;
            }
        }
        else
            min[++minPtr] = x;

    }

    void pop() {
        if(topPtr < 0)      //Underflow
            return;

        topPtr -= 1;
        minPtr -= 1;
    }

    int top() {
        return stack[topPtr];
    }

    int getMin() {
        return min[minPtr];
    }
}
