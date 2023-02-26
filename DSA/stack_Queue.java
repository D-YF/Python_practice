import java.util.*;

public class stack_Queue {
    static Stack<Integer> stc1 = new Stack<Integer>();
    static Stack<Integer> stc2 = new Stack<Integer>();

    void Enqueue(int value){
        stc1.push(value);
    }

    int Dequeue(){
        if (stc1.isEmpty() && stc2.isEmpty())
            return Integer.MIN_VALUE;
        
        if (!stc2.isEmpty()){
            int item = stc2.pop();
            return item;
        }
        else{
            while(!stc1.isEmpty()){
                stc2.push(stc1.pop());
            }
            int item = stc2.pop();
            return item;
        }
    }
    
}
