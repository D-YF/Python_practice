# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = ListNode(next=head), ListNode(next=head)
        dummy = slow

        while fast and n:
            fast = fast.next
            n -= 1
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        N1 = 0
        N2 = 0

        dummy_A = ListNode(next=headA)
        dummy_B = ListNode(next=headB)

        curA, curB = dummy_A, dummy_B

        while curA.next:
            N1 += 1
            curA = curA.next
        while curB.next:
            N2 += 1
            curB = curB.next

        dif = abs(N1-N2)

        curA, curB = dummy_A, dummy_B
        while dif and curA.next and curB.next:
            if N1>N2:
                curA = curA.next
            else:
                curB = curB.next
            dif -= 1
        
        while curA and curB:
            if curA==curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        N = len(nums)

        i = 0
        ans = []

        for i in range(N-2):
            if ans and ans[-1][0]==nums[i]:
                continue

            left = i+1
            right = N-1

            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    if ans and ans[-1][0]==nums[i] and ans[-1][1]==nums[left]:
                        left += 1
                        continue
                    else: 
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1
                else:
                    if nums[i]+nums[left]+nums[right]>0:
                        right -= 1
                    else:
                        left += 1
        return ans

# nums = [-1,0,1,0,1,2,-1,-4]
# sol = Solution()
# print(sol.threeSum(nums))
                

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        N = len(nums)

        ans = []

        for i in range(N-3):
            if ans and ans[-1][0] == nums[i]:
                continue

            for k in range(i+1, N-2):
                if ans and ans[-1][0]==nums[i] and ans[-1][1]==nums[k]: continue
                
                left = k+1
                right = N-1
                while left<right:
                    if nums[i]+nums[k]+nums[left]+nums[right]==target:
                        if ans and ans[-1][0]==nums[i] and ans[-1][1]==nums[k] and ans[-1][2]==nums[left]:
                            left += 1
                            continue
                        else:
                            ans.append([nums[i], nums[k], nums[left], nums[right]])
                            left += 1
                    
                    elif nums[i]+nums[k]+nums[left]+nums[right]<target:
                        left += 1
                    else:
                        right -= 1
        
        return ans

# nums = [1,0,-1,0,-2,2]
# target = 0
# sol = Solution()
# print(sol.fourSum(nums, target))

# from collections import deque
# queue = deque(['A', 'B', 'C'])
# print(queue.popleft())


class MyQueue:

    def __init__(self):
        self.Instack = []
        self.Outstack = []

    def push(self, x: int) -> None:
        self.Instack.append(x)

    def pop(self) -> int:
        if self.empty(): return None

        if not self.Outstack:
            while self.Instack:
                self.Outstack.append(self.Instack.pop())

        return self.Outstack.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.Outstack.append(ans)

        return ans

    def empty(self) -> bool:
        return not (self.Instack or self.Outstack)

# stack = MyQueue()
# stack.push(1)
# stack.push(2)
# print(stack.peek())
# print(stack.pop())
# print(stack.empty())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty(): return None

        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        
        return self.queue.popleft()
            

    def top(self) -> int:
        top = self.pop()
        # print("Top is" + str(top))
        self.queue.append(top)
        return top

    def empty(self) -> bool:
        return not self.queue

# # Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# print(obj.top())
# print(obj.pop())
# print(obj.empty())

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False

        stack = []
        for item in s:
            if item=='(':
                stack.append(')')
            elif item=='[':
                stack.append(']')
            elif item=='{':
                stack.append('}')
            else:
                if not stack or stack.pop() != item:
                    return False
            # elif item==')':
            #     if not stack or stack.pop() != '(':
            #         return False
            # elif item==']':
            #     if not stack or stack.pop() != '[':
            #         return False
            # elif item=='}':
            #     if not stack or stack.pop() != '{':
            #         return False

        return True if not stack else False

s = "()[][{()}]"
sol = Solution()
print(sol.isValid(s))

