from typing import List, Optional

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0:1}

        prefix_sum = 0
        ans = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum-k in hash:
                ans += hash[prefix_sum-k]
            
            # Dictionary, just put the argument posionally
            # Don't use hash.get(prefix_sum, default = 0)
            hash[prefix_sum] = hash.get(prefix_sum, 0) + 1

        return ans