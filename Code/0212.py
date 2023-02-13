from typing import List, Optional

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = [0] * (k+1)
        rows = len(nums)
        dp[0] = 1
        count = 0

        for i in range(rows):
            for j in range(k, 0, -1):
                if i==0 or (dp[j-nums[i]] and dp[j-nums[i]-nums[i-1]]):
                    dp[j] +=  dp[j-nums[i]]
        return dp[-1]

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        ans = 0

        for i in range(l):
            total = 0
            for j in range(i, l, 1):
                total += nums[j]
                if total == k:
                    ans += 1
                    if j<l-1 and nums[j+1]==0:
                        continue
                    else:
                        break

        return ans


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # recursive
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root==None: return 0

            right = dfs(root.right)
            left = dfs(root.left)

            return max(right, left)+1
        
        return dfs(root)


class Solution:
    # iterative
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def preoerder(root, depth):
            nonlocal ans
            if root==None: return

            if depth>ans:
                ans = depth
            
            if root.left:
                preoerder(root.left, depth+1)
            if root.right:
                preoerder(root.right, depth+1)
            
            return
        preoerder(root, ans)
        return ans

class Solution:
    # iterative
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        queue = deque()
        ans = 0

        queue.append(root)
        while queue:
            ans += 1
            l = len(queue)

            for i in range(l):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans