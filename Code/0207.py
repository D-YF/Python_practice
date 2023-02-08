from typing import List, Optional

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for str in strs:
            zeros, ones = 0, 0
            for c in str:
                if c=='1': ones += 1
                else: zeros += 1
            
            for i in range(n, ones-1, -1):
                for j in range(m , zeros-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-ones][j-zeros] + 1)
            
        return dp[-1][-1]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], amount+1, 1):
                dp[j] += dp[j-coins[i]]

        return dp[-1]