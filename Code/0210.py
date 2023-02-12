class Solution:
    def climbStairs(self, n: int) -> int:
        items = [1, 2]

        dp = [0]*(n+1)
        dp[0] = 1

        for j in range(n+1):
            for i in range(len(items)):
                if j-items[i]>=0:
                    dp[j] += dp[j-items[i]]
        
        return dp[-1]


