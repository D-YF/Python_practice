from typing import List,Optional

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        ans = []

        def isValid(s):
            if len(s)==0 or len(s)>3  :
                return False
            if s[0]=='0' and len(s)>1:
                return False
            if not 0<= int(s) <= 255:
                return False
            
            return True

        def traceback(s, startIndex):
            if len(path)==4:
                if startIndex==len(s):
                    ans.append(".".join(path[:]))
                    return
            
            for i in range(startIndex, len(s)):
                ## Trim!!!
                if len(path)>3:
                    return
                temp = s[startIndex:i+1]
                if  isValid(temp):
                    path.append(temp[:])
                    traceback(s, i+1)
                    path.pop()
                else:
                    return
        if len(s)>12:
            return []
        traceback(s, 0)
        return ans

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = [[]]

        def traceback(nums, startIndex):
            if startIndex>=len(nums):
                return
            
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                ans.append(path[:])
                traceback(nums, i+1)
                path.pop()
            return
        
        traceback(nums, 0)
        return ans


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = [[]]
        nums.sort()

        def traceback(nums, startIndex):

            for i in range(startIndex, len(nums)):
                if i>startIndex and nums[i]==nums[i-1]:
                    continue
                
                path.append(nums[i])
                ans.append(path[:])
                traceback(nums, i+1)
                path.pop()
            
            return
        
        traceback(nums, 0)
        return ans