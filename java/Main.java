import java.util.Scanner;

import javax.imageio.stream.ImageOutputStream;

import java.util.*;
import java.time.*;
import java.util.ArrayList;
import java.util.Collections;


class vehicle{
    String name;
}

public class Main extends vehicle {
    int x;
    enum Size{
        Small,
        Medium,
        Big
    }
    
    public Main(int y){
        x = y;
    }
    
    public static void main(String[] args){
        LocalTime time = LocalTime.now();
        Scanner st = new Scanner(System.in);
        // String username = st.nextLine();

        Main myObj = new Main(99);
        
        int s = sum(5);
        System.out.println(s);
        // myObj.x = 20;
        System.out.println(myObj.x);
        for (Size size : Size.values()){
            System.out.println(size);
        }

        System.out.println(time);

        st.close();

        ArrayList<String> cars = new ArrayList<String>();
        cars.add("Toyata");
        cars.add("Mini");
        cars.add("BMW");
        Collections.sort(cars);
        iterate(cars);

        String my_str = "I think I need more practice!";
        String reverse = "";
        String[] split = my_str.split(" ", 7);
        for (String word: split)
            System.out.println(word);

        for (int i=0; i<my_str.length(); i++){
            reverse = my_str.charAt(i) + reverse;
        }
        System.out.println(reverse);


        Stack<String> my_stack = new Stack<String>();
        my_stack.push("ch");
        my_stack.push("abc");
        System.out.println(my_stack.search("ch"));
        System.out.println(my_stack);


        int my_test = 5;
        System.out.println(my_test/2);

    }

    static int sum(int n){
        if (n==0) return 0;
        else return n+sum(n-1);
    }


    static void iterate(ArrayList<String> cars){
        System.out.println(cars.size());

        for (String str: cars){
            System.out.println(str);
        }
    }

}


// class Solution {
//     public void rotate(int[] nums, int k) {
//         k %= nums.length;
//         reverse(nums, 0, nums.length-1);
//         reverse(nums, 0, k-1);
//         reverse(nums, k, nums.length-1);
//     }

//     void reverse(int[] nums, int l, int r){
//         while(l<r){
//             int temp = nums[l];
//             nums[l] = nums[r];
//             nums[r] = temp;
//             l++;
//             r--;
//         }

//     }
// }


// class Solution {
//     public int findMin(int[] nums) {
//         int index = 0;

//         for (int i=1; i<nums.length; i++){
//             if(nums[i]<nums[i-1])
//                 index = i;
//         }
//         return nums[index];
//     }
// }

// class Solution {
//     public int findMin(int[] nums) {
//         int left = 0;
//         int right = nums.length-1;
//         while (left < right){
//             int mid = (left+right)/2;
//             if (nums[mid]<nums[right])
//                 right = mid;
//             else
//                 left = mid;
//         }

//         return nums[left];
//     }
// }


// class Solution {
//     public int findMin(int[] nums) {
//         int left = 0;
//         int right = nums.length - 1 ;
//         while(left<right){
//             int mid = (left + right)/2;

//             if (nums[mid] > nums[right])
//                 left = mid+1;
//             else if(nums[mid] < nums[right]) 
//                 right = mid;
//             else
//                 right ++;
//         }

//         return nums[left];
//     }
// }


// class Solution {
//     public int search(int[] nums, int target) {
//         int left = 0;
//         int right = nums.length - 1;

//         while (left<=right){
//             int mid = (left+right)/2;
//             if (nums[mid]==target) return mid;

//             if (nums[left]<= nums[mid]){
//                 if(nums[left] <= target && target < nums[mid])
//                     right = mid-1;
//                 else
//                     left = mid+1;
//             }
//             else{
//                 if (nums[mid]< target && target <= nums[right] ){
//                     left = mid+1;
//                 }
//                 else{
//                     right = mid-1;
//                 }
//             }
//         }

//         return -1;
//     }
// }