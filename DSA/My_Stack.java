public class My_Stack {
    static final int MAX = 1000;
    int size;
    int[] stack = new int[MAX];

    My_Stack(){
        size = 0;
    }

    public boolean isEmpty()
    {
        return (size==0) ? true : false;
    }

    public void push(int value){
        if (size >= MAX){
            System.out.println("Stack overflow!");
        }
        else{
            stack[size++] = value;
            System.out.println(value + " is pushed into stack!");
        }
    }

    public int pop(){
        if (isEmpty()){
            System.out.println("Stack is empty!");
            return 0;
        }
        else{
            System.out.println("Current size is " + size);
            int value = stack[size-1];
            size --;
            System.out.println(value + " is poped out!");
            return value;
        }

    }

    public int peek(){
        if (isEmpty()){
            System.out.println("Stack is empty!");
            return 0;
        }
        else{
            return stack[size-1];
        }
    }

    



}
