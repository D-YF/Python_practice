public class Main {
    public static void main(String args[]){
        /* 
        My_Stack stack = new My_Stack();
        System.out.println(stack.isEmpty());
        stack.push(0);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(5);
        
        System.out.println(stack.isEmpty());

        int peek1 = stack.peek();
        System.out.println("Current peek is " + peek1);

        int poped = stack.pop();
        System.out.println(poped);

        int peek2 = stack.peek();
        System.out.println("Current peek is " + peek2);
        */
        
        My_Queue queue = new My_Queue();
        System.out.println(queue.isEmpty());
        queue.Enqueue(0);
        queue.Enqueue(1);
        queue.Enqueue(2);
        queue.Enqueue(3);

        queue.Front();
        queue.Rear();

        queue.Dequeue();
        queue.Dequeue();
        queue.Dequeue();
        queue.Dequeue();
        System.out.println(queue.isEmpty());
    }
}
