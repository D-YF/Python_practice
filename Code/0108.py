# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None:
            return
        
        dummy_head = ListNode(next=head)
        slow, fast = dummy_head, dummy_head

        while n>=0:
            if fast==None:
                return None
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy_head.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLength(self, head):
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        curA = headA
        curB = headB

        diff = abs(lenA-lenB)
        while diff:
            if lenA>lenB:
                curA = curA.next
            else:
                curB = curB.next
            diff -= 1
        while curA and curB:
            if curA==curB:
                return curA
            curA = curA.next
            curB = curB.next
            
        return None
    

