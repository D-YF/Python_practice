class Solution(object):
    # use two points -- O(n^2)
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

# nums = [-1,0,1,2,-1,-4]
# sol = Solution()
# print(sol.threeSum(nums))


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums = sorted(nums)
        ans = []

        for i in range(N-3):
            if ans and nums[i] == ans[-1][0]: continue

            for j in range(i+1, N-2):
                if ans and nums[i] == ans[-1][0] and nums[j] == ans[-1][1]: continue
            
                left = j+1
                right = N-1
                
                while  left<right:
                    if nums[i]+nums[j]+nums[left]+nums[right]==target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left += 1
                        while left<right and nums[right]==nums[right-1]:
                            right -= 1
                    
                    if nums[i]+nums[j]+nums[left]+nums[right] < target:
                        left += 1
                    else:
                        right -= 1
                
        return ans

nums = [1,0,-1,0,-2,2]
target = 0
sol = Solution()
print(sol.fourSum(nums, target))