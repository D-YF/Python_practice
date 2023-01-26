from typing import List, Optional

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        
        def traceback(candidates, value):
            if value==0:
                ans.append(path[:])
                return
            elif value<0:
                return
            
            for i in range(len(candidates)):
                path.append(candidates[i])
                traceback(candidates[i:], value-path[-1])
                path.pop()
            return
        traceback(candidates, target)
        return ans

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans= []
        path = []
        candidates.sort()

        def traceback(candidates, value, start):
            if value==0:
                ans.append(path[:])
                return
            if value<0:
                return
            
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                traceback(candidates, value-path[-1], i+1)
                path.pop()
            return
        
        traceback(candidates, target, 0)
        return ans


class Solution:
    def isPelindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left<right:
            if s[left] != s[right]:
                return False
            left  += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def traceback(s, startIndex):
            if startIndex>=len(s):
                ans.append(path[:])
                return

            for i in range(startIndex, len(s)):
                temp = s[startIndex:i+1]
                if self.isPelindrome(temp):
                    path.append(temp[:])
                    traceback(s, i+1)
                    path.pop()
                else:
                    continue

        traceback(s, 0)
        return ans