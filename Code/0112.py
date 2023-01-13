class Solution(object):
    def getKMParray(self, s):
        s = list(s)
        N = len(s)
        length = 0
        i = 1
        LPS = [0]*N

        while i < N:
            # This logic is hard to understand
            if s[i]==s[length]:
                length += 1
                LPS[i] = length
                i += 1
            else:
                if length==0:
                    LPS[i] = 0
                    i += 1
                else:
                    # pay attention to this line
                    length = LPS[length-1]
        return LPS

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        LPS = self.getKMParray(s)
        N = len(LPS)
        max = LPS[-1]
        if max>=(N-max) and max%(N-max)==0:
            return True
        else:
            return False

# s = "abac"
# sol = Solution()
# print(sol.getKMParray(s))
# print(sol.repeatedSubstringPattern(s))

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur, fast = 0, 0
        N = len(nums)

        while fast<N:
            if nums[fast] != val:
                nums[cur] = nums[fast]
                cur += 1
                fast += 1
            else:
                fast += 1
        return cur
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# sol = Solution()
# print(sol.removeElement(nums, val))



class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)

        left = 0
        right = N-1
        while left<right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1

# s = ["h","e","l","l","o"]
# sol = Solution()
# sol.reverseString(s)
# print(s)


class Solution:
    def replaceSpace(self, s: str) -> str:
        N = len(s)

        i = N-1
        while i>=0:
            if s[i]==' ':
                s = s[:i] + "%20" + s[i+1:]
            i -= 1
        return s

# s = "We are happy."
# sol = Solution()
# print(sol.replaceSpace(s))


class Solution:
    def reverse(self, s: list) -> None:
        N = len(s)
        left, right = 0, N-1
        
        while left<right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1
        return s
    
    def reverseWords(self, s: str) -> str:
        s = list(s)
        self.reverse(s)

        N_origin = len(s)
        left, right = 0, N_origin-1
        while left<right and (s[left]==' ' or s[right] ==' '):
            if s[left]==' ': left += 1
            if s[right] == ' ': right -= 1
        
        s = s[left:right+1]
        N_new = len(s)
        
        s_onespace = []
        for i in range(N_new):
            if s[i] != ' ':
                s_onespace.append(s[i])
            else:
                if s[i-1] != ' ':
                    s_onespace.append(' ')
                else:
                    continue
        
        N_final = len(s_onespace)
        left = 0
        for i in range(N_final):
            if i+1 == N_final:
                s_onespace[left: i+1] = self.reverse(s_onespace[left: i+1])
            elif s_onespace[i]==' ':
                s_onespace[left: i] = self.reverse(s_onespace[left: i])
                left = i+1

        return "".join(s_onespace)

# s = "  the   sky is blue  "
# sol = Solution()
# print(sol.reverseWords(s))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recursive(pre: ListNode, cur: ListNode):
            if cur==None: return pre

            temp = cur.next
            cur.next = pre
            recursive(cur, temp)

        pre = None
        cur = head
        return recursive(pre, cur)


