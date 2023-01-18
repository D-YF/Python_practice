from typing import List,Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        if root==None:
            return []
        
        stack.append(root)
        ans = []

        while stack:
            node = stack.pop()

            if node != None:
                if node.right:
                    stack.append(node.right)
                
                if node.left:
                    stack.append(node.left)

                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop()
                ans.append(node.val)
        
        return ans


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []

        if root==None:
            return []
        
        stack.append(root)

        while stack:
            node = stack.pop()
            if node != None:
                if node.right:
                    stack.append(node.right)
                
                stack.append(node)
                stack.append(None)

                if node.left:
                    stack.append(node.left)
            
            else:
                node = stack.pop()
                ans.append(node.val)
        
        return ans


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []

        if root:
            stack.append(root)
        
        while stack:
            node = stack.pop()
            if node != None:
                stack.append(node)
                stack.append(None)
            
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                ans.append(node.val)
            
        return ans