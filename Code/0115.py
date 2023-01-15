from typing import List

class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []

        for item in s:
            if ans and ans[-1]==item:
                ans.pop()
            else:
                ans.append(item)
        
        return "".join(ans)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = list(s)
        slow, fast = 0, 0
        N = len(ans)

        while fast<N:
            ans[slow] = ans[fast]

            if slow>0 and ans[slow]==ans[slow-1]:
                slow -= 1
            else:
                slow += 1
            fast += 1

        return "".join(ans[:slow])


# s = "abbacee"
# sol = Solution()
# print(sol.removeDuplicates(s))

from operator import add, sub, mul

class Solution:
    # RPN: Reverse Polish Notion
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        operator = {'+':add, '-':sub, '*':mul, '/':lambda x,y: int(x/y)}

        for item in tokens:
            if item not in operator:
                ans.append(int(item))
            else:
                operand2 = ans.pop()
                operand1 = ans.pop()
                ans.append(operator[item](operand1, operand2))
            # if ans and item == '+':
            #     operand2 = ans.pop()
            #     operand1 = ans.pop()
            #     ans.append(operand1 + operand2)
            # elif ans and item == '-':
            #     operand2 = ans.pop()
            #     operand1 = ans.pop()
            #     ans.append(operand1 - operand2)
            # elif ans and item == "*":
            #     operand2 = ans.pop()
            #     operand1 = ans.pop()
            #     ans.append(operand1 * operand2)
            # elif ans and item == "/":
            #     operand2 = ans.pop()
            #     operand1 = ans.pop()
            #     ans.append(int(operand1 / operand2))
            # else:
            #     ans.append(int(item))
        return ans.pop()

# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# # tokens = ["4","13","5","/","+"]
# sol = Solution()
# print(sol.evalRPN(tokens))

from collections import deque
class Mydeque():
    def __init__(self) -> None:
        self.queue = deque()
    
    def pop(self, value):
        if self.queue and value==self.queue[0]:
            self.queue.popleft()
    
    def push(self, value):
        ## Make sure myqueue is in ascending order
        while self.queue and value>self.queue[-1]:
            self.queue.pop()

        self.queue.append(value)
    
    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        N = len(nums)
        myqueue = Mydeque()
        for i in range(k):
            myqueue.push(nums[i])

        ans.append(myqueue.front())

        for i in range(k, N):
            myqueue.pop(nums[i-k])
            myqueue.push(nums[i])

            ans.append(myqueue.front())
            i += 1
        return ans

# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# sol = Solution()
# print(sol.maxSlidingWindow(nums, k))

import heapq
q = []
heapq.heappush(q, (1,2))
heapq.heappush(q, (4,4))
heapq.heappush(q, (1,2))
heapq.heappush(q, (2,2))
heapq.heappop(q)
# print(q)

class Solution:
    ## My First priority queue using heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for item in nums:
            hashmap[item] = hashmap.get(item, 0) + 1
        
        pri_que = []

        for key, freq in hashmap.items():
            heapq.heappush(pri_que, [freq, key])

            if len(pri_que)>k:
                heapq.heappop(pri_que)

        ans = []
        for item in pri_que:
            ans.append(item[1])
        
        return ans

nums = [1, 2, 2, 3, 5, 5, 2, 2]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))
