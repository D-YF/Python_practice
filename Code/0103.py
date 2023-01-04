class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [-1] * length
        left = 0
        right = length-1

        while left <= right:
            if nums[left]**2 > nums[right]**2:
                result[length-1] = nums[left]**2
                left += 1
            else:
                result[length-1] = nums[right]**2
                right -= 1
            length -= 1 
        return result
nums = [-4,-1,0,3,10]
sol = Solution()
print(sol.sortedSquares(nums))
