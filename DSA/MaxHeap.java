
public class MaxHeap {
    /*
     * heapify
     * insertion
     * deletion / remove max|min
     * getMAX or getMIN
     */

    // children of i-th Node : 2*i+1 2*i+2
    int[] arr;
    int maxSize;
    int heapSize;

    static void buildHeap(int[] arr, int N){
        // N-1 = 2*i + 1  -->  i = N/2 - 1
        int startIndex = N/2-1;
        for (int i=startIndex; i>=0; i--){
            heapify(arr, i);
        }

    }    

    
    static void heapify(int[] arr, int i){
        int N = arr.length;
        int leftChild = 2*i+1;
        int rightChild = 2*i+2;
        
        int maxIndex = i;

        if(leftChild<N && arr[leftChild]>arr[maxIndex]){
            maxIndex = leftChild;
        }

        if(rightChild<N && arr[rightChild]>arr[maxIndex]){
            maxIndex = rightChild;
        }

        if(maxIndex != i){
            int temp = arr[i];
            arr[i] = arr[maxIndex];
            arr[maxIndex] = temp;

            heapify(arr, maxIndex);
        }

    }

    int parent(int i){
        return (i-1)/2;
    }

    void Insertion(int data){
        if(heapSize==maxSize){
            System.out.println("The heap is full!");
        }

        heapSize ++;
        int i = heapSize-1;
        arr[i] = data;
        while(parent(i)>=0 && arr[i]>arr[parent(i)]){
            int temp = arr[i];
            arr[i] = arr[parent(i)];
            arr[parent(i)] = temp;

            i = parent(i);
        }
    }

    int removeMax(){
        if(heapSize<=0)
            return Integer.MAX_VALUE;

        int maxvalue = arr[0];
        arr[0] = arr[heapSize-1];
        heapSize--;

        heapify(arr, 0);
        return maxvalue;
    }

    static void printHeap(int arr[], int N)
    {
        System.out.println(
            "Array representation of Heap is:");
  
        for (int i = 0; i < N; ++i)
            System.out.print(arr[i] + " ");
  
        System.out.println();
    }

    MaxHeap(int maxSize){
        this.maxSize = maxSize;
        arr = new int[maxSize];
        heapSize = 0;
    }


}
