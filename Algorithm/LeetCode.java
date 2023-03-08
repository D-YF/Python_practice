import javax.smartcardio.TerminalFactory;

import java.util.*;

public class LeetCode {
    
}

class Solution1 {
    public int integerBreak(int n) {
        int[] dp = new int[n+1];
        dp[0] = 1;
        for(int i=0; i<=n; i++){
            dp[i] = 0;
        }
        // Iterate bags
        for(int i=1; i<=n; i++){
            // Iterate items, could be duplicate
            for(int j=i; j<=n; j++){
                // No break: dp[i] 
                // Break   : 
                //  -- i * dp[j-i] break (j-i) as well 
                //  -- i * (j-i)   not break (j-i)
                int value1 = Math.max(dp[j], (i)*dp[j-i]);
                dp[j] = Math.max(value1, i*(j-i));
            }
        }
        return dp[n];
    }
}
class Solution2 {
    public long countFairPairs(int[] nums, int lower, int upper) {
        long ans = 0;
        int N = nums.length;
        Arrays.sort(nums);
        for(int i=0; i<N-1; i++){
            int num1 = nums[i];
            int right_edge = upper-num1;
            int left_edge = lower-num1;
            int l = i+1;
            int r = N-1;
            int right_index = searchUpper(nums, l, r, right_edge);
            int left_index = searchLower(nums, l, r, left_edge);
            ans += (right_index - left_index) + 1;
        }
        return ans;
    }

    int searchUpper(int[] nums, int l, int r, int target){
        while(l<=r){
            int mid = (l+r)/2;
            if(nums[mid]>target)
                r =  mid - 1;
            else
                l = mid + 1;
        }
        return r;
    }

    int searchLower(int[] nums, int l, int r, int target){
        while(l<=r){
            int mid = (l+r)/2;
            if(nums[mid]<target)
                l = mid + 1;
            else
                r =  mid - 1;
        }
        return l;
    }

}

class Solution3 {
    int ans = Integer.MIN_VALUE;
    public int bestTeamScore(int[] scores, int[] ages) {
        int[][] arr = new int[scores.length][2];
        for(int i=0; i<scores.length; i++){
            arr[i][0] = ages[i];
            arr[i][1] = scores[i];
        }

        Arrays.sort(arr, new Comparator<int[]>() {
            public int compare(int[] a1, int[] a2){
                if(a1[0]==a2[0]){
                    return (a1[1]-a2[1]);
                }
                return a1[0]-a2[0];  
            }
        });

        int N = scores.length;
        int[] dp = new int[N];

        for(int i=0; i<N; i++){
            dp[i] = arr[i][1];
        }
        // Iterate Pack first, items later
        for(int i=0; i<N; i++){
            for(int j=0; j<i; j++){
                if(arr[j][1] <= arr[i][1]){
                    // 
                    dp[i] = Math.max((dp[j]+arr[i][1]), dp[i]);
                }
            }
            ans = Math.max(ans, dp[i]);
        }

        return ans;
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

class Solution4 {
    public ListNode reverseEvenLengthGroups(ListNode head) {
        int cur_N = 1;
        ListNode cur_Node = head;
        // pre Node -> head
        ListNode pre = new ListNode(0, cur_Node);
        while(pre != null){
            int count = 0;
            ListNode dummy = pre;
            // count even or odd
            for(int i=0; i<cur_N; i++){
                if(dummy.next != null){
                    count ++;
                    dummy = dummy.next;
                }
            }
            // if even, then reverse
            if(count % 2 ==0){
                pre = reverse(pre, count);
            }
            //else continue
            else
                pre = dummy;
            //next group
            cur_N ++;
        }
        return head;
    }

    ListNode reverse(ListNode last_group, int length){
        ListNode next_group = new ListNode();

        ListNode pre = last_group.next;
        if(pre==null)
            return null;
        ListNode cur = pre.next;
        ListNode future_tail = pre;
        for(int i=0; i<length-1; i++){
            if(i==length-2){
                next_group = cur.next;
            }
            ListNode next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;        
        }
        //updata this group head and tail
        last_group.next = pre;
        future_tail.next = next_group;
        // return tail of this group 
        // as the pre Node of next group
        return future_tail;
    }

}


class Solution5 {
    public int findMaximumXOR(int[] nums) {
        int ans = Integer.MIN_VALUE;
        for(int i=0; i<nums.length; i++){
            for(int j=i; j<nums.length; j++){
                int cur = nums[i]^nums[j];
                ans = (cur > ans) ? cur : ans;
            }
        }
        return ans;
    }
}

class Solution6 {
    public int findMaximumXOR(int[] nums) {
        int ans = Integer.MIN_VALUE;
        int max_num = nums[0];
        for(int i=1; i<nums.length; i++){
            // max_num = (nums[i]>max_num) ? nums[i] : max_num;
            max_num = Math.max(nums[i], max_num);
        }    

        for(int i=0; i<nums.length; i++){
            // ans = ((max_num^nums[i])>ans) ? (max_num^nums[i]): ans;
            ans = Math.max(max_num^nums[i], ans);
        }
        return ans;
    }
}

class Solution7 {
    public int openLock(String[] deadends, String target) {
        // Edge case 1
        if(target.equals("0000"))
            return 0;
        
        HashSet<String> dead = new HashSet<String>();
        for(String str : deadends){
            dead.add(str);
        }
        
        // Edge case 2
        if(dead.contains("0000"))
            return -1;

        int step = 0;
        HashSet<String> path = new HashSet<String>();
        Queue<String> queue = new LinkedList<String>();
        queue.add("0000");
        path.add("0000");
        // bfs using queue
        // Each while loop is a same level (step)
        while(!queue.isEmpty()){
            int size = queue.size();
            // Iterate all nodes in current level
            for(int i=0; i<size; i++){
                String cur = queue.poll();
                // Target Solution
                if(cur.equals(target))
                    return step;
                // All possible Next step
                for(String next:getNext(cur)){
                    if(!path.contains(next) && !dead.contains(next)){
                        queue.add(next);
                        path.add(next);
                    }
                }
            }
            step++;
        }
        // No solution
        return -1;
    }

    char Upnext(char c){
        return (c=='9') ? '0' : (char) (c+1);
    }

    char Downnext(char c){
        return (c=='0') ? '9' : (char) (c-1);
    }

    List<String> getNext(String cur){
        List<String> ans = new ArrayList<>();
        char[] arr = cur.toCharArray();
        for(int i=0; i<4; i++){
            char c = arr[i];

            arr[i] = Upnext(c);
            ans.add(new String(arr));

            arr[i] = Downnext(c);
            ans.add(new String(arr));
            // restore character
            arr[i] = c;
        }
        return ans;
    }

}


class Solution8 {
    List<List<Integer>> ans = new ArrayList<>();
    // LinkedList has method to remove last element .removerLast();
    LinkedList<Integer> path = new LinkedList<>();
    public List<List<Integer>> subsets(int[] nums) {
        backtraking(nums, 0);
        return ans;
    }

    // start_index to avoid dumplicate element
    void backtraking(int[] num, int start_index){
        // Important to CLONE path before adding to ans
        ans.add(new ArrayList<>(path));
        if(start_index==num.length){
            return;
        }
        for(int i=start_index; i<num.length; i++){
            path.add(num[i]);
            // next start_index i+1
            backtraking(num, i+1);
            path.removeLast();
        }
    }

}

class Solution {
    public String addSpaces(String s, int[] spaces) {
        char[] arr = s.toCharArray();
        int n = arr.length;
        int l = spaces.length;
        char[] ans = new char[n+l];

        // original string index
        int i=n-1;
        // new string index
        int j=ans.length-1;
        int space_index = l-1;

        while(i>=0){
            // add space
            if(i==spaces[space_index]){
                ans[j--] = arr[i--];
                ans[j--] = ' ';
                space_index --;
            }
            // copy
            else
                ans[j--] = arr[i--];
        }

        return String.valueOf(ans);
    }
}