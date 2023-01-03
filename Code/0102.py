class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left<right:
            mid = (left+right)//2
            if nums[mid]>target:
                right = mid
            elif nums[mid]<target:
                left = mid+1
            else:
                return mid
        return -1

nums = [5]
target = 5
sol = Solution()
# print(sol.search(nums, target))


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        flag = -1
        count = 0
        while val in nums:
            ## List.index() is O(n)!!!
            nums[nums.index(val)] = nums[flag]
            nums[flag] = None
            flag -= 1
        return (len(nums)+flag+1)

class Solution:
    def removeElement(self, nums, val):
        slow = 0
        fast = 0
        while fast<len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

nums = [3,2,2,3]
val = 3
sol = Solution()
print(sol.removeElement(nums, val))