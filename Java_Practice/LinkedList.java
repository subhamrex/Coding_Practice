package Java_Practice;

public class LinkedList {
    Node head;
    public void insert(int data){
        Node node = new Node();
        node.data = data;
        node.next = null; // By default it's null. we don't have to do that

        if (head == null){
            head = node;
        }
        else{
            Node n = head; // temp node
            while(n.next != null){
                n = n.next;
            }
            n.next = node;

        }

    }
    public void show(){
        Node node = head;
        while(node.next != null){
            System.out.println(node.data);
            node=node.next;
        }
        System.out.println(node.data);
    }

    public void insertAtFirst(int data){
        Node node = new Node();
        node.data = data;
        node.next = null; // By default it's null. we don't have to do that
        node.next = head;
        head = node;

    }

    public void insertAt(int index,int data){
        Node node = new Node();
        node.data = data;
        node.next = null; // By default it's null. we don't have to do that

        if (index == 0){
            insertAtFirst(data);
        }
        else{
            Node n = head;
            for(int i = 0;i<index-1;i++){
                n = n.next;
            }
            node.next = n.next;
            n.next = node;
        }

    }

    public void deleteAt(int index){
        if(index == 0){
            head = head.next;
        }
        else{
            Node n = head;
            Node n1 = null;
            for(int i = 0;i<index-1;i++){
                n = n.next;
            }
            n1 = n.next;
            n.next = n1.next;
            System.out.println(" Deleted data: "+n1.data);


        }
    }
}
