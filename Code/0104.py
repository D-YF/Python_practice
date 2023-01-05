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

nums = [1,2,3,4,5]
target = 15
sol = Solution()
print(sol.minSubArrayLen(target,nums))