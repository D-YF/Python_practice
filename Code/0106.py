# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

# recursive
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def recursive(pre, cur):
            if not cur:
                return pre
            
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            return recursive(pre, cur)
        
        pre = None
        cur = head
        return recursive(pre, cur)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(next=head)
        pre = result
        
        while pre.next and pre.next.next:
            cur = pre.next
            later = pre.next.next

            pre.next = later

            cur.next = later.next

            later.next = cur

            pre = pre.next.next

        return result.next