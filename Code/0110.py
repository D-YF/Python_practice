class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length<3: return None

        nums, result = sorted(nums), []

        for i in range(length-2):
            left = i+1
            right = length-1
            if result and result[-1][0]==nums[i]: continue

            while(left < right):
                if nums[i]+nums[left]+nums[right]==0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left += 1
                    while left<right and nums[right]==nums[right-1]:
                        right -= 1
                
                if nums[i]+nums[left]+nums[right]<0:
                    left += 1
                else:
                    right -= 1

        return result

nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))


