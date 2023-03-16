import java.util.*;

import javax.security.auth.login.CredentialException;


public class LeetCode2 {
    
}

class Solution1 {
    public int partitionString(String s) {
        int N = s.length();
        int index = 0;
        int ans = 1;

        int[] hash = new int[26];
        Arrays.fill(hash, 0);

        while(index<N){
            int ascII = (int) s.charAt(index)-'a';
            if(hash[ascII]!=0){
                ans ++;
                Arrays.fill(hash, 0);
            }
            hash[ascII] ++;
            index ++;
        }
        return ans;
        
    }
}


class Solution2 {
    public int minimumSize(int[] nums, int maxOperations) {
        int l = 1;
        int r = Integer.MIN_VALUE;
        for(int num:nums){
            r = Math.max(r, num);
        }

        while(l<r){
            int mid = l + (r-l)/2;
            if(check(nums, mid, maxOperations))
                r = mid;
            else
                l = mid+1;
        }
        return r;

    }

    boolean check(int[] nums, int target, int operations){
        for(int num: nums){
            // partition_times = (value-1)/target
            operations -= (num-1)/target;
        }
        return operations>=0;
    }

}


class Solution3 {
    public boolean isValid(String s) {
        int[] table = new int[3];
        Arrays.fill(table, 0);

        for(char ch:s.toCharArray()){
            table[(int) ch-'a'] ++;
            if(check(table)==false)
                return false;
        }
        return true;
    }

    boolean check(int[] table){
        if(table[0]<table[1] || table[1]<table[2] || table[0]<table[2])
            return false;
        return true;
    }

}


class Solution4 {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for(char ch:s.toCharArray()){
            stack.push(ch);
            if(stack.peek()=='c'){
                stack.pop();
                if(stack.size()>=2){
                    char b = stack.pop();
                    char a = stack.pop();
                    if(b!='b' || a!='a')
                        return false;
                }
                else
                    return false;
            }
        }
        return stack.empty();
    }
}


class Solution {
    private int[] ans;
    private int len;


    public int[] executeInstructions(int n, int[] startPos, String s) {
        len = s.length();
        ans = new int[len];

        for(int i=0; i<s.length(); i++){
            iterate(n, startPos, i, s);
        }
        return ans;

    }

    void iterate(int n, int[] start_pose, int start_index, String s){
        int path_count = 0;
        for(int i=start_index; i<s.length(); i++){
            start_pose = nextPos(start_pose, s.charAt(i));
            if(checkValid(start_pose, n)){
                path_count++;
            }
            else
                break;
        }
        ans[start_index] = path_count;
    }

    int[] nextPos(int[] current_pos, char instruction){
        int[] next = new int[2];
        if(instruction=='U'){
            next[0] = current_pos[0]-1;
            next[1] = current_pos[1];
        }
        else if(instruction=='D'){
            next[0] = current_pos[0]+1;
            next[1] = current_pos[1];
        }
        else if(instruction=='R'){
            next[0] = current_pos[0];
            next[1] = current_pos[1]+1;
        }
        else if(instruction=='L'){
            next[0] = current_pos[0];
            next[1] = current_pos[1]-1;
        }
        return next;
    }

    boolean checkValid(int[] pos, int n){
        if(pos[0]>=n || pos[0]<0 || pos[1]>=n || pos[1]<0)
            return false;
        return true;
    }

}


class Solution {
    public long countBadPairs(int[] nums) {
        long ans = 0;
        for(int i=0; i<nums.length-1; i++){
            for(int j=i+1; j<nums.length; j++){
                if(j-i != nums[j]-nums[i])
                    ans++;
            }
        }
        return ans;
    }
}


class Solution {
    public long countBadPairs(int[] nums) {
        int n = nums.length;
        long ans = n*(n-1)/2;
        HashMap<Integer, Integer> hash = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int dif = i-nums[i];
            hash.put(dif, hash.getOrDefault(dif, 0)+1);
        }
        for(int value:hash.values()){
            ans -= (long) value*(value-1)/2;
        }
        return ans;
    }
}


class Solution {
    public int[] arrayChange(int[] nums, int[][] operations) {
        int n = nums.length;
        HashMap<Integer, Integer> hash = new HashMap<>();
        for(int i=0; i<n; i++){
            hash.put(nums[i], i);
        }
        for(int[] ope:operations){
            int origin = ope[0];
            int target = ope[1];
            int index = hash.get(origin);

            nums[index] = target;
            hash.remove(origin);
            hash.put(target, index);
        }
        return nums;
    }
}


class Solution {
    public int minElements(int[] nums, int limit, int goal) {
        long sum = 0;
        for(int num:nums){
            sum += (long) num;
        }

        long target = Math.abs(goal-sum);
        long ans = 0;
        
        ans = (long) target/limit;
        target = (long) target % limit;

        if(target != 0)
            ans ++;

        return (int) ans;
    }
}



// Definition for singly-linked list.
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public int numComponents(ListNode head, int[] nums) {
        HashSet<Integer> hash = new HashSet<>();
        for(int num:nums){
            hash.add(num);
        }

        ListNode dummy = head;
        int ans = 0;

        while(!hash.isEmpty() && dummy!=null){
            if(hash.contains(dummy.val)){
                ans ++;
                while(!hash.isEmpty() && dummy!=null && hash.contains(dummy.val)){
                    hash.remove(dummy.val);
                    dummy = dummy.next;
                }
            }
            else
                dummy = dummy.next;
        }
        return ans;

    }
}


class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n+1];
        int len = 1;
        dp[1] = nums[0];
        for(int i=1; i<n; i++){
            int num = nums[i];
            if(num>dp[len]){
                dp[++len] = num;
            }
            else{
                int l=1;
                int r=len;
                int pos=1;
                while(l<=r){
                    int mid = l + (r-l)/2;
                    if(dp[mid] < num){
                        l = mid + 1;
                        pos = l;
                    }
                    else{
                        r = mid - 1;
                    }
                }
                dp[pos] = num;
            }
        }
        return len;
    }
}


class Solution {
    // incomplete
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n+1];
        int[] dp_count = new int[n+1];

        dp[1] = nums[0];
        dp_count[1] = 1;
        int len = 1;

        for(int i=1; i<n; i++){
            int num = nums[i];
            if(dp[len] < num){
                dp[++len] = num;
                dp_count[len] = dp_count[len-1];
            }
            else{
                int l = 1;
                int r = len;
                int pos = 1;
                while(l<=r){
                    int mid = l + (r-l)/2;
                    if(dp[mid]<num){
                        l = mid+1;
                        pos = mid;
                    }
                    else{
                        r = mid - 1;
                    }
                }
                dp[pos] = num;
                dp_count[pos] = dp_count[pos] + 1;
            }
        }

        return dp_count[len];
    }
}


