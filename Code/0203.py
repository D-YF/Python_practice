from typing import List

class Solution:
    def fib(self, n: int) -> int:
        if n<=1 : return n

        pre = 0
        cur = 1
        n = 2
        while n-2>0:
            
            ind = cur
            cur = cur+pre
            pre = ind
            n -= 1
        return cur


class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp = [0]*(n+1)

        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+2):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n+1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[len(cost)]