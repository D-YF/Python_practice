from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child = 0
        cookie = 0
        ans = 0

        while child<len(g) and cookie<len(s):
            if s[cookie]>=g[child]:
                ans += 1
                cookie += 1
                child += 1
            else:
                cookie += 1
        return ans



class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count = 1
        pre_dif = 0
        cur_index = 0
        while cur_index+1 < len(nums):
            cur_dif = nums[cur_index+1]-nums[cur_index]
            if pre_dif*cur_dif <= 0 and cur_dif!=0:
                count += 1
                pre_dif = cur_dif
                cur_index += 1
            else:
                cur_index += 1
        
        return count

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("INF")
        sum = 0

        for num in nums:
            sum += num
            if sum>ans:
                ans = sum
            if sum<=0:
                sum = 0
        return ans


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        index = 1

        while index<len(prices):
            if prices[index]>prices[index-1]:
                ans += prices[index] - prices[index-1]
            index += 1
        return ans


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            cur = i+nums[i]
            if farthest>=i:
                farthest = max(farthest, cur)
                if farthest>=len(nums)-1:
                    return True
        return False


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: return 0

        cur_farthest = nums[0]
        next_farthest = 0
        steps = 1

        for i in range(len(nums)):
            if i >cur_farthest:
                steps += 1
                cur_farthest = next_farthest

            cur = nums[i]+i
            if cur>next_farthest:
                next_farthest = cur

            if cur_farthest>=len(nums)-1:
                return steps