from typing import List,Optional

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ans = 0

        minPrice = prices[0]
        for i in range(1, len(prices)):

            minPrice = min(minPrice, prices[i])

            if prices[i]-minPrice <= fee:
                continue
            else:
                ans += prices[i]-minPrice-fee
                minPrice = prices[i] - fee
        
        return ans


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.ans = 0
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(cur: TreeNode) -> int:
            if cur==None: return 2

            left = dfs(cur.left)
            right = dfs(cur.right)

            if left==2 and right==2:
                return 0
            elif left==1 or right==1:
                return 2
            elif left==0 or right==0:
                self.ans += 1
                return 1
        if dfs(root)==0:
            self.ans += 1
        return self.ans