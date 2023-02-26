import java.util.*;

public class my_Hash {
    public static void main(String args[]){
        // Not encouraged
        Hashtable<Integer, String> 
            hm = new Hashtable<Integer, String>();
        
        hm.put(1, "Learning");
        hm.put(12, "for");
        hm.put(15, "Data");
        hm.put(6, "Structure");

        System.out.println(hm);

        int[] arr = {1,2,3,12,1,2,31,2,2,6,23,12};
        printFreq(arr);
        
        HashSet<String> hash_set = new HashSet<String>();
        hash_set.add("abc");
        hash_set.add("abc");
        hash_set.add("ab");
        System.out.println(hash_set);

    }

    static void printFreq(int[] arr){
        HashMap<Integer, Integer> 
            my_hash = new HashMap<Integer, Integer>();
        
        for(int i=0; i<arr.length; i++){
            if (my_hash.get(arr[i]) == null)
                my_hash.put(arr[i], 1);
            else{
                int counts = my_hash.get(arr[i]);
                my_hash.put(arr[i], counts+1);
            }
        }

        for (Map.Entry<Integer, Integer> m: my_hash.entrySet()){
            System.out.println("Frequency of " + m.getKey() +
                " is " + m.getValue());
        }


    }

}
