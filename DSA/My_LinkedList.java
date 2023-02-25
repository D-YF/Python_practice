class Node{
    int data;
    Node next;
    
    // initialize
    Node(int d)
    {
        data = d;
        next = null;
    }
}

public class My_LinkedList {
    // This method prints the linked list
    public static void printList(Node head) {
        System.out.println("[" + "Node.data" + "] [" + "Node" + "]->" + "(Next)"); // Print the node value and null
        while (head != null) { // Loop through the linked list
        if (head.next == null) { // If the current node is the last node
            System.out.println("[" + head.data + "] [" + head + "]->" + "(null)"); // Print the node value and null
        } else {
            System.out.println("[" + head.data + "] [" + head + "]->" + head.next); // Print the node value and the next node
        }
        head = head.next; // Move to the next node
        }
        System.out.println();
        System.out.println();
    }

    public static Node PushNode(Node head, int data){
        // Insert at the beginning
        Node cur = new Node(data);
        cur.next = head;
        return cur;

    }

    public static Node DeleteNode(Node head, int position){
        Node temp = head;
        Node pre = head;
        if (position==1){
            return head.next;
        }

        for (int i=0; i<position; i++){
            if (i==position-1 && temp != null){
                pre.next = temp.next;
                break;
            }
            else{
                pre = temp;
                if(pre==null)
                    break;
                temp = temp.next;
            }



        }
        return head;

    }

    public static boolean SeachNode(Node head, int data){
        Node temp = head;
        while (temp != null){
            if (temp.data==data){
                return true;
            }
            temp = temp.next;
        }
        return false;
    }

    public static void main(String args[]){
        // push Node in front of head Node
        Node head = new Node(3);
        head = PushNode(head, 2);
        head = PushNode(head, 1);
        head = PushNode(head, 0);
        printList(head);

        // Delete a node in certain postion
        DeleteNode(head, 2);
        printList(head);

        // Check if List contains a data
        System.out.println(SeachNode(head, 1));

    }
    
}


