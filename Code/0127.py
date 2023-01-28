from typing import List, Optional

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []

        def traceback(nums):
            if len(path)==len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if not nums[i] in path:
                    path.append(nums[i])
                    traceback(nums)
                    path.pop()
                else:
                    continue
            return
        
        traceback(nums)
        return ans
        
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []

        def traceback(nums, used):
            if len(path)==len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if (i>0 and nums[i]==nums[i-1] and used[i-1]==False):
                    continue

                if used[i]==False:
                    used[i] = True
                    path.append(nums[i])
                    traceback(nums, used)
                    path.pop()
                    used[i] = False
            return

        nums.sort()
        used = [False]*len(nums)
        traceback(nums, used)
        return ans




class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        # dect for list!
        dic = defaultdict(list)

        for ticket in tickets:
            dic[ticket[0]].append(ticket[1])

        for airport in dic:
            dic[airport].sort()
        
        path = ["JFK"]

        def traceback(departure):
            if len(path)==len(tickets)+1:
                return True
            
            for destination in dic[departure]:
                dic[departure].pop(0)
                path.append(destination)
                if traceback(destination):
                    return True
                path.pop()
                
                dic[departure].append(destination)
                dic[departure].sort()

            return
        
        traceback("JFK")
        return path