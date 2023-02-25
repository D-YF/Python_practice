import java.text.NumberFormat.Style;

public class My_Queue {
    int MAX = 1000;
    int front;
    int rear;
    int[] queue = new int[MAX];

    My_Queue(){
        front = 0;
        rear = 0;
    }

    boolean isEmpty(){
        return (rear==front);
    }

    int Front(){
        if (isEmpty()){
            System.out.println("The queue is empty!");
            return Integer.MIN_VALUE;
        }
        else
            System.out.println("The Front is " + queue[front]);
            return queue[front];
    }
    
    int Rear(){
        if (isEmpty()){
            System.out.println("The queue is empty!");
            return Integer.MIN_VALUE;
        }
        else{
            System.out.println("The Rear is " + queue[rear-1]);
            return queue[rear-1];
        }
    }

    void Enqueue(int value){
        if (rear==MAX){
            System.out.println("The queue is full!");
        }
        else{
            queue[rear++] = value;
            System.out.println(value + " has been enqueued!");
        }
    }

    int Dequeue(){
        if (isEmpty()){
            System.out.println("The queue is empty!");
            return Integer.MAX_VALUE;
        }
        else{
            int value = queue[front];
            for (int i=front; i<rear-1; i++){
                queue[i] = queue[i+1];
            }
            rear --;
            System.out.println(value + " has been dequeued!");
            return value;
        }
    }

}
