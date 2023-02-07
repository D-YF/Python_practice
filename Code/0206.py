from typing import List, Optional

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = int(total/2)
        rows = len(stones)

        dp = [0]*(target+1)
        
        for i in range(rows):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        
        return total-dp[target] - dp[target]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        rows = len(nums)

        if (total + target)%2==1: return 0
        if abs(target)>total: return 0

        sum1 = int((total + target)/2)

        dp = [0] * (sum1+1)
        dp[0] = 1
        for i in range(rows):
            for j in range(sum1, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        
        return dp[-1]