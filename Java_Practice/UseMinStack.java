package Java_Practice;

public class UseMinStack {


    public static void main(String[] args) {
        MinStack obj = new MinStack();
        obj.push(10);
        obj.pop();
        int param_3 = obj.top();
        int param_4 = obj.getMin();
        System.out.println(param_3);
        System.out.println(param_4);
    }
}
