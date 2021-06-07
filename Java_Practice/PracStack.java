

import java.net.SocketOption;

public class PracStack {
    public static void main(String[] args) {
        Stack nums = new Stack();
        nums.push(14);
        nums.push(15);
        nums.push(17);
        System.out.println("Peeked Element: " +nums.peek());
        nums.push(16);
        nums.push(18);
        System.out.println("Pooped Element:"+nums.pop());
        System.out.println("Size: "+nums.size());
        System.out.println("Stack is empty : "+nums.isEmpty());

        nums.show();
    }
}
