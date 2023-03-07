import java.util.ArrayList;

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

        for(int i=1; i<=n; i++){
            for(int j=i; j<=n; j++){
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


