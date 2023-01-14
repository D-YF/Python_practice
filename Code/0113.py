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

nums = [-1,0,1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))
                

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        