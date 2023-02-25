import java.util.ArrayList;
import java.util.List;

public class My_Array {
    public static int LinearSearch(int[] arr, int target){
        // O(N)
        int result = -1;
        for (int i=0; i<arr.length; i++){
            if (arr[i]==target)
                result = i;
        }
        return result;
    }

    public static void ReverseArray(int[] arr){
        // O(N)
        int left = 0;
        int right = arr.length-1;
        while(left<right){
            int temp = arr[right];
            arr[right] = arr[left];
            arr[left] = temp;
            right--;
            left++;
        }
    }

    public static void printArray(int[] arr){
        for (int i=0; i<arr.length; i++){
            System.out.print(arr[i] + " ");
        }
    }

    public static void LeftRotate(int[] arr, int step){
        int N = arr.length;
        
        ReverseArray(arr);

        int left = 0;
        int right = N - step - 1;
        while(left < right){
            int temp = arr[right];
            arr[right] = arr[left];
            arr[left] = temp;
            right--;
            left++;
        }

        left = N-step;
        right = N-1;
        while(left < right){
            int temp = arr[right];
            arr[right] = arr[left];
            arr[left] = temp;
            right--;
            left++;
        }
        printArray(arr);
    }

    public static void RightRotate(int[] arr, int step){
        int N = arr.length;
        
        ReverseArray(arr);

        int left = 0;
        int right = step-1;
        while(left < right){
            int temp = arr[right];
            arr[right] = arr[left];
            arr[left] = temp;
            right--;
            left++;
        }

        left = step;
        right = N-1;
        while(left < right){
            int temp = arr[right];
            arr[right] = arr[left];
            arr[left] = temp;
            right--;
            left++;
        }
        printArray(arr);
    }

    public static int BinarySearch(int[] arr, int target){
        int left = 0;
        int right = arr.length-1;
        while(left<=right){
            int mid = (left+right)/2;
            if (arr[mid] == target){
                System.out.println("Find it in " + mid);
                return mid;
            }
            else if (arr[mid]>target)
                right = mid - 1;
            else
                left = mid + 1;
        }
        
        System.out.println("Not found!");
        return -1;
    }

    public static void BubbleSort(int[] arr){
        int N = arr.length;
        for (int i=0; i<N-1; i++){
            for (int j=0; j<N-i-1; j++){
                if(arr[j]>arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }

    }

    public static void Merge(int[] arr, int left, int mid, int right){
        // O(NlogN)
        // Merge sort is generally considered 
        // better when data is huge and stored in external storage.
        // Stable than Quick sort
        int N1 = mid - left + 1;
        int N2 = right - mid;
        int[] L = new int[N1];
        int[] R = new int[N2];

        for (int i=0; i<N1; i++){
            L[i] = arr[left+i];
        }
        for (int i=0; i<N2; i++){
            R[i] = arr[mid+i+1];
        }

        int i=0;
        int j=0;
        int k=0;
        while(i<N1 && j<N2){
            if(L[i]<=R[j]){
                arr[left + k] = L[i];
                i++;
            }
            else {
                arr[left + k] = R[j];
                j++;
            }
            k++;
        }

        while(i<N1){
            arr[left + k] = L[i];
            i++;
            k++;
        }
        while(j<N2){
            arr[left + k] = R[j];
            j++;
            k++;
        }

    }

    public static void MergeSort(int[] arr, int left, int right){
        if (left<right){
            int mid = (left + right)/2;
            MergeSort(arr, left, mid);
            MergeSort(arr, mid+1, right);

            Merge(arr, left, mid, right);
        }
    }

    public static void Swap(int[] arr, int index1, int index2){
        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }

    public static void QuickSort(int[] arr, int left, int right){
        // O(nlogN)
        // Worst case O(N^2), not stabel
        // It uses extra space only for storing recursive function calls
        // But still in-place algorithm
        if (right<left)
            return;
        int pivot = arr[right];
        int k=left-1;
        for (int i=left; i<right; i++){
            if(arr[i]<pivot){
                k++;
                Swap(arr, i, k);
            }
        }
        // Not clear about edge operation
        Swap(arr, right, ++k);
        QuickSort(arr, left, k-1);
        QuickSort(arr, k+1, right);
    }


    public static void main(String args[]){

        // Test case for linear searching
        int[] arr1= {5, 2, 4, 1, 6, 2, 0, 9};
        int target1 = 0;
        int target2 = 10;
        int index1 = LinearSearch(arr1, target1);
        int index2 = LinearSearch(arr1, target2);
        if (index1==-1)
            System.out.println("The element is not present in array!");
        else
            System.out.println(target1 + " is in " + index1);
        if (index2==-1)
            System.out.println("The element is not present in array!");
        else
            System.out.println(target2 + " is in " + index2);

        System.out.println();

        // Build function of ArrayList
        List<Integer> arr2 = new ArrayList<Integer>();
        arr2.add(5);
        arr2.add(10);
        int target3 = 0;
        if (arr2.contains(target3))
            System.out.println(target3 + " is in arr2");
        else
            System.out.println("No in arr2");
        
        // Test case for reversing
        int[] arr3 = {5, 2, 4, 1, 6, 2, 0, 9};
        ReverseArray(arr3);
        printArray(arr3);
        System.out.println();

        // Test case for Left rotation
        int[] arr4 = {1, 2, 3, 4, 5, 6};
        LeftRotate(arr4, 4);
        System.out.println();
        
        // Test case for Right rotation
        int[] arr5 = {1, 2, 3, 4, 5, 6};
        RightRotate(arr5, 4);
        System.out.println();

        // Test case for binary search
        int[] arr6 = {2, 3, 5, 6, 7, 8, 9, 12, 17, 20};
        BinarySearch(arr6, 7);

        // Bubble sort
        int[] arr7 = {2, 3, 3, 5, 2, 6, 6, 1, 0};
        BubbleSort(arr7);
        printArray(arr7);
        System.out.println();

        // Merge sort
        int[] arr8 = {2, 3, 3, 5, 2, 6, 6, 1, 0};
        MergeSort(arr8, 0, arr8.length-1);
        printArray(arr8);
        System.out.println();

        // Quick Sort
        int[] arr9 = {2, 4, 5, 2, 3, 6, 1, 0, 1, 0, 9, 12};
        QuickSort(arr9, 0, arr9.length-1);
        printArray(arr9);
        System.out.println();


    }
}
