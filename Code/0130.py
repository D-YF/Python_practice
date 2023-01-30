from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i in range(len(nums)):
            if (nums[i]<0 and k>0):
                nums[i] = -nums[i]
                k -= 1
            else:
                break
        
        if k%2==1:
            nums.sort()
            nums[0] = -nums[0]
        
        return sum(nums)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        cur_sum = 0
        total_sum = 0

        for i in range(len(gas)):
            rest = gas[i]-cost[i]
            cur_sum += rest
            total_sum += rest

            if cur_sum<0:
                start = i+1
                cur_sum = 0
        
        if total_sum<0: return -1
        return start


class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                ans[i] = ans[i-1]+1
        
        for i in range(len(ratings)-2, -1):
            if ratings[i]>ratings[i+1]:
                ans[i] = max(ans[i],ans[i+1]+1)

        return sum(ans)