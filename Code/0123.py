from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def postorder(root):
            if root == None: return None

            left = postorder(root.left)
            right = postorder(root.right)
            
            # return the highest node
            if root==p or root==q:
                return root
            
            if left and right:
                return root
            if left and right==None:
                return left
            else:
                # contain None
                return right
        
        return postorder(root)
