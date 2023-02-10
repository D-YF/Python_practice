from typing import List, Optional

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1

        for j in range(nums[i], target+1, 1):
            for i in range(len(nums)):
                dp[j] += dp[j-nums[i]]

        return dp[-1]