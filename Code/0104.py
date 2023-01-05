class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        N = len(nums)
        cur_sum = nums[left]
        minlen = N

        while right < N:
            if cur_sum<target:
                right += 1
                if right<N:
                    cur_sum += nums[right]
                continue

            while cur_sum >= target:
                if (right-left+1)<minlen:
                   minlen = right-left+1
                
                if nums[right]>nums[left]:
                    cur_sum -= nums[left]
                    left += 1
                else:
                    right += 1
                    if right==N:
                        break
                    cur_sum += nums[right]
                    cur_sum -= nums[left]
                    left += 1
        if minlen==N and sum(nums)<target:
            return 0
        return minlen

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        minlen = float("inf")
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            while cur_sum >= target:
                minlen = min(i-left+1, minlen)
                cur_sum -= nums[left]
                left += 1

        return 0 if minlen==float("inf") else minlen


nums = [1,1,1,1]
target = 5
sol = Solution()
print(sol.minSubArrayLen(target,nums))