from typing import  List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None: return False

        def dfs(root, curSum):
            curSum += root.val
            if root.left==None and root.right==None and curSum == targetSum:
                return True
            if root.left:
                if dfs(root.left, curSum): return True
            if root.right:
                if dfs(root.right, curSum): return True
            
            return False

        ans = dfs(root, 0)
        return ans

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(root : TreeNode, curPath: List) -> None:
            curSum = sum(curPath)
            
            if root.left==None and root.right==None and curSum==targetSum:
                # curPath is incorrect
                # should be curPath[:]
                ans.append(curPath[:])
                return
            
            if root.left:
                curPath.append(root.left.val)
                dfs(root.left, curPath)
                curPath.pop()
            if root.right:
                curPath.append(root.right.val)
                dfs(root.right, curPath)
                curPath.pop()
            return
        ans = []
        if root==None:
            return []
        Curpath = [root.val]
        dfs(root,Curpath)
        return ans

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0:
            return None
        
        root_val = postorder[-1]
        root = TreeNode(val=root_val)

        root_index = inorder.index(root_val)

        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index+1:]

        post_left = postorder[:len(inorder_left)]
        post_right = postorder[len(inorder_left): len(postorder)-1]

        root.left = self.buildTree(inorder_left, post_left)
        root.right = self.buildTree(inorder_right, post_right)
        
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder==None:
            return None
        
        root_val = preorder[0]
        root = TreeNode(val=root_val)

        index = inorder.index(root_val)

        inorder_left = inorder[:index]
        inorder_right = inorder[index+1:]

        preorder_left = preorder[1: len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root