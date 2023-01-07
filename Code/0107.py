# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
# Recursive!!!
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        leftmax = self.maxDepth(root.left)
        rightmax = self.maxDepth(root.right)

        return max(leftmax,rightmax)+1

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

        if head==None or head.next==None:
            return head
        
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head

        return temp


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxlen(self, root):
        if root==None:
            return 0
        return max(self.maxlen(root.left), self.maxlen(root.right))+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        left_maxlen = self.maxlen(root.left)
        right_maxlen = self.maxlen(root.right)
        if abs(left_maxlen - right_maxlen)>1 or (not self.isBalanced(root.left)) or (not self.isBalanced(root.right)):
            return False
        return True