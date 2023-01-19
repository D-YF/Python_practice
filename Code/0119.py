from typing import Liss, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if left==None or right ==None:
                return left == right

            check_val = (left.val == right.val)
            check_out = check(left.left, right.right)
            check_in  = check(left.right, right.left)

            return check_val and check_out and check_in
        
        return check(root.left, root.right)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compare(left, right):
            if left==None or right==None:
                return left == right
            
            check_val = (left.val == right.val)
            check_left = compare(left.left, right.left)
            check_right = compare(left.right, right.right)
            return check_val and check_left and check_right
        return compare(p, q)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1, root2):
            if root1==None or root2==None:
                return (root1==root2)
            
            check_val = (root1.val==root2.val)
            check_left = isSame(root1.left, root2.left)
            check_right = isSame(root1.right, root2.right)
            return check_val and check_left and check_right
        
        self.ans = False
        
        def isSub(root, subRoot):
            check_root, check_left, check_right = False, False, False

            if root==None or subRoot==None:
                return root==subRoot
            
            if root.val == subRoot.val:
                check_root = isSame(root, subRoot)
            
            check_left = isSub(root.left, subRoot)
            check_right = isSub(root.right, subRoot)
            return check_root or check_right or check_left
        self.ans = isSub(root, subRoot)
        return self.ans


class Solution:
    def __init__(self) -> None:
        self.ans = 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def preorder_depth(root, depth):
            if root==None:
                return None

            self.ans = depth if depth>self.ans else self.ans

            if root.left:
                preorder_depth(root.left, depth+1)
            if root.right:
                preorder_depth(root.right, depth+1)
            return None
        
        if root==None: return 0
        preorder_depth(root, 1)
        return self.ans

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self) -> None:
        self.maxD = 0

    def maxDepth(self, root: 'Node') -> int:
        def preorder(root, depth):
            if root==None:
                return None
            self.maxD = depth if depth>self.maxD else self.maxD

            for child in root.children:
                preorder(child, depth+1)
            return None

        if root==None: return 0
        preorder(root, 1)
        return self.maxD