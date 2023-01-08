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
        
        fast = ListNode(next=head)
        slow = fast

        while n>=0:
            if fast==None:
                return None
            fast = fast.next
            n -= 1
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return head