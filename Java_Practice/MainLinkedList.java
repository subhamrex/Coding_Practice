package Java_Practice;

public class MainLinkedList {
    public static void main(String[] args) {
    LinkedList ll = new LinkedList();
    ll.insert(5);
    ll.insert(6);
    ll.insert(7);
    ll.insert(8);
    ll.insertAtFirst(22);
    ll.insertAt(2,56);
    ll.insertAt(0,99);
    ll.deleteAt(2);

    ll.show();
    }
}
