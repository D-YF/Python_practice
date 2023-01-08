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



#######################################################
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


#######################################################
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


#######################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self, left, right):
        if left==None or right==None:
            return left is right

        check_val = (left.val == right.val)
        return (check_val and self.check(left.left, right.right) and self.check(left.right, right.left))

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root.left, root.right)


#######################################################
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0 

        if root.left == None:
            minlength = self.minDepth(root.right)+1
        elif root.right == None:
            minlength = self.minDepth(root.left)+1
        else:
            minlength = min(self.minDepth(root.left), self.minDepth(root.right))+1
        
        return minlength  



#######################################################
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp
    
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



#######################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1==None:
            return root2
        if root2==None:
            return root1

        merged = TreeNode(root1.val+root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)

        return merged


#######################################################
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        
        max_value = max(nums)
        index = nums.index(max_value)

        root = TreeNode(val=max_value)
        root.left = self.constructMaximumBinaryTree(nums[0: index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])

        return root



#######################################################
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
    
        if head.val==head.next.val:
            head.next = head.next.next
            self.deleteDuplicates(head)

        self.deleteDuplicates(head.next)
        return head

## Non recursive
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head

        cur = head

        while (cur and cur.next):
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head