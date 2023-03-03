import javax.xml.stream.EventFilter;

import java.lang.annotation.Target;
import java.util.*;

public class Algorithm {
    public static void printArray(int[] arr){
        for (int i=0; i<arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static int BinarySearch(int[] arr, int target){
        int N = arr.length;
        int left = 0;
        int right = N-1;

        while(left<=right){
            int mid = (left+right)/2;
            if(arr[mid]==target)
            {
                System.out.println("The traget " + target
                 + " is in index " + mid);
                return mid;
            }
            
            if(arr[mid]>target)
                right = mid-1;
            else
                left = mid+1;

        }

        System.out.println("Not find the target!");
        return -1;
    }

    static void BubbleSort(int[] arr){
        for (int i=0; i<arr.length; i++){
            for(int j=0; j<arr.length-i-1; j++){
                if(arr[j]>arr[j+1]){
                    swap(arr, j, j+1);
                }
            }
        }
        printArray(arr);
    }


    static void SelectionSort(int[] arr){
        int N = arr.length;
        for (int i=0; i<N-1; i++){
            int minIndex = i;
            for(int j=i+1; j<N; j++){
                if(arr[j] < arr[minIndex]){
                    minIndex = j;
                }
            }
            swap(arr, i, minIndex);
        }
        printArray(arr);
    }

    static void InsertionSort(int[] arr){
        int N = arr.length;
        for (int i=1; i<N; i++){
            for (int j=i; j>0; j--){
                if(arr[j]<arr[j-1])
                    swap(arr, j, j-1);
            }
        }
        printArray(arr);
    }

    static void QuickSort(int[] arr, int left, int right){
        int pivot = arr[right];
        int Index = left;

        for (int i=left; i<=right; i++){
            if(arr[i]<pivot){
                swap(arr, i, Index);
                Index ++;
            }
        }
        swap(arr, right, Index);
        if((Index-1)>left)
            QuickSort(arr, left, Index-1);
        if((Index+1)<right)
            QuickSort(arr, Index+1, right);
    }

    static void MergeSort(int[] arr, int left, int right){
        if(left>=right)
            return;

        int mid = (left+right)/2;

        MergeSort(arr, left, mid);
        MergeSort(arr, mid+1, right);
        Merge(arr, left, mid, right);
    }

    static void Merge(int[] arr, int left, int mid, int right){
        int[] arr1 = new int[mid-left+1];
        int[] arr2 = new int[right-mid];
        
        for(int i = 0; i<mid-left+1; i++){
            arr1[i] = arr[i+left];
        }
        for(int i = 0; i<right-mid; i++){
            arr2[i] = arr[i+mid+1];
        }
        int k = 0;
        int i = 0;
        int j = 0;
        int[] reslut = new int[right-left+1];

        // printArray(arr);
        while(i<mid-left+1 && j<right-mid){
            if(arr1[i]<arr2[j]){
                reslut[k++] = arr1[i++];
            }
            else
                reslut[k++] = arr2[j++];
        }
        while(i<mid-left+1){
            reslut[k++] = arr1[i++];
        }
        while(j<right-mid){
            reslut[k++] = arr2[j++];
        }
        for (int a=0; a<reslut.length; a++){
            arr[left+a] = reslut[a];
        }

    }


    public static void towerOfHanoi(int N, char start, char end, char helper){
        if (N==1){
            System.out.println("Move disk from " + start + " to " + end);
            return;
        }
        towerOfHanoi(N-1, start, helper, end);

        System.out.println("Move disk from " + start + " to " + end);

        towerOfHanoi(N-1, helper, end, start);
    }

    public static void main(String args[]){
        // Test case for binary searching
        System.out.println("Test case for Binary searching:");
        int arr1[] = {};
        int arr2[] = {1};
        int arr3[] = {1, 2, 3, 5};
        BinarySearch(arr1, 1);
        BinarySearch(arr2, 1);
        BinarySearch(arr3, 3);

        //Test case for Bubble sort
        //Dumplicate / Unique
        System.out.println("Test case for Bubble sort:");
        int arr5[] = {1};
        int arr6[] = {1, 4, 2, 2, 1, 5, 6};
        BubbleSort(arr5);
        BubbleSort(arr6);

        //Test case for Selection sort
        System.out.println("Test case for Selection sort:");
        int arr7[] = {2};
        int arr8[] = {2, 1, 0};
        SelectionSort(arr7);
        SelectionSort(arr8);

        //Test case for Insertion sort
        System.out.println("Test case for Insertion sort:");
        int arr9[] = {2};
        int arr10[] = {4, 2, 13, 2, 2, 5, 0, 1};
        InsertionSort(arr9);
        InsertionSort(arr10);

        //Tese case for Quick sort
        System.out.println("Test case for Quick sort:");
        int arr11[] = {4, 2, 1, 4, 3, 6, 3, 3, 9};
        int arr12[] = {4};
        QuickSort(arr11, 0, arr11.length-1);
        QuickSort(arr12, 0, arr12.length-1);
        printArray(arr11);
        printArray(arr12);
        
        //Test case for merge sort
        System.out.println("Test case for Merge sort:");
        int arr13[] = {4, 2, 1, 4, 3, 6, 3, 3, 9};
        int arr14[] = {5};
        MergeSort(arr13, 0, arr13.length-1);
        MergeSort(arr14, 0, arr14.length-1);
        printArray(arr13);
        printArray(arr14);

        //Test case for tower of Hamnoi
        towerOfHanoi(3, 'A', 'C', 'B');
        
    }

}



class Item {
    int value, weight;
    Item(int x, int y){
        this.value = x;
        this.weight = y;
    }
}


class Solution
{
    //Function to get the maximum total value in the knapsack.
    double fractionalKnapsack(int W, Item arr[], int n) 
    {
        Arrays.sort(arr, new Comparator<Item>(){
            @Override
            public int compare(Item i1, Item i2){
                double ratio1 = (double) i1.value/i1.weight;
                double ratio2 = (double) i2.value/i2.weight;
                // Ascending
                return (ratio1>ratio2) ? 1 : -1;
            }
        });

        double ans = 0.;
        for (int i=n-1; i>=0; i--){
            if(arr[i].weight <= W){
                ans += arr[i].value;
                W -= arr[i].weight;
            }
            else{
                double ratio = W/arr[i].weight;
                ans += arr[i].value * ratio;
                break;
            }
        }
        return ans;
   }
}
