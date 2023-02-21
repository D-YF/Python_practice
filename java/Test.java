class Queue {
    int front, rear, size;
    int capacity;
    int[] arr;

    public Queue(int capacity){
        this.capacity = capacity;
        this.front = this.size = 0;
        this.rear = capacity-1;
        this.arr = new int[this.capacity];
    }

    boolean isfull(Queue queue){
        return (queue.size == queue.capacity);
    }

    boolean isEmpty(Queue queue){
        return (queue.size==0);
    }

    void enqueue(int item){
        if (isfull(this)) 
            return;
        this.rear = (this.rear + 1) % this.capacity;
        this.arr[this.rear] = item;
        this.size ++;
        System.out.println("Enqueue " + item + " to queue");
    }

    int dequeue(){
        if (isEmpty(this))
            return Integer.MIN_VALUE;
        
        int item = this.arr[this.front];
        this.front = (this.front + 1 ) % this.capacity;
        this.size --;
        System.out.println("Dequeue " + item + " Out");
        return item;

    }
    

}


public class Test{
    public static void main(String[] args){
        Queue queue = new Queue(1000);
        System.out.println(queue.capacity);
        queue.enqueue(10);
        queue.enqueue(20);
        queue.dequeue();

    }
}