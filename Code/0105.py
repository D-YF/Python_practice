class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0]*n for _ in range(n)]
        loop = n//2 # the number of circles
        startx, starty = 0, 0
        value = 1

        for offset in range(1, loop+1):
            for i in range(starty, n-offset):
                result[startx][i] = value
                value += 1
            
            for i in range(startx, n-offset):
                result[i][n-offset] = value
                value += 1

            for i in range(n-offset, starty, -1):
                result[n-offset][i] = value
                value += 1

            for i in range(n-offset, startx, -1):
                result[i][starty] = value
                value += 1

            startx += 1
            starty += 1
        
        if n%2 == 1:
            result[loop][loop] = value
        return result

n = 1
sol = Solution()
print(sol.generateMatrix(n))

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(next=head)
        cur = new_head

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return new_head.next
        
head = [], val = 1