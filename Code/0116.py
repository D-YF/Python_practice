from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def preorder(root: Optional[TreeNode], result: List[int]):
            if root==None:
                return
            result.append(root.val)
            preorder(root.left, result)
            preorder(root.right, result)
        
        result = []
        preorder(root, result)
        return result

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return result


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(root, result):
            if root == None:
                return
            
            result.append(root.val)
            inorder(root.left, result)
            inorder(root.right, result)
        
        result = []
        inorder(root, result)
        return result


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []

        cur = root
        while cur!=None or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        
        return ans


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root, result):
            if root == None:
                return
            
            postorder(root.left, result)
            postorder(root.right, result)
            result.append(root.val)
        
        result = []
        postorder(root, result)
        return result

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return ans[::-1]