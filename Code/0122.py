from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1==None and root2==None:
            return None
        
        if root1 and root2:
            root1.val += root2.val
        elif root1==None and root2:
            root1 = TreeNode(val=root2.val)
        
        if root2:
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
        else:
            root1.left = self.mergeTrees(root1.left, None)
            root1.right = self.mergeTrees(root1.right, None)

        return root1

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1==None: return root2
        if root2==None: return root1

        merged = TreeNode(val=root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)

        return merged



class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None: return None

        if root.val==val: return root

        if root.left:  
            left_ans = self.searchBST(root.left, val)
            if left_ans: return left_ans
        if root.right: 
            right_ans = self.searchBST(root.right, val)
            if right_ans: return right_ans

        return None

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None: return None

        if root.val == val: return root

        if val>root.val:
            node = self.searchBST(root.right, val)
            if node:
                return node
        else:
            node = self.searchBST(root.left, val)
            if node:
                return node
        return None


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        max_val = -float('INF')
        def dfs(root):
            nonlocal max_val
            if root==None: return True

            left = dfs(root.left)

            if root.val>max_val:
                max_val = root.val
            else:
                return False
            
            right = dfs(root.right)
            return left and right
        
        return dfs(root)


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        ans = float("INF")
        pre = None
        def Traversal(curNode):
            nonlocal pre, ans
            if curNode==None: return None

            Traversal(curNode.left)
            
            if pre:
                ans = min(curNode.val - pre.val, ans)
            pre = curNode

            Traversal(curNode.right)
            return None
        
        Traversal(root)
        return ans

class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.preNode = None
        self.maxNum = 0
        self.count = 0
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if root==None: return None

            traverse(root.left)
            
            curNode = root
            if self.preNode==None:
                self.count = 1
            elif curNode.val==self.preNode.val:
                self.count += 1
            else:
                self.count = 1
            self.preNode = curNode

            if self.count==self.maxNum:
                self.ans.append(curNode.val)
            elif self.count>self.maxNum:
                self.maxNum = self.count
                self.ans.clear()
                self.ans.append(curNode.val)
            
            traverse(root.right)
            return None

        traverse(root)

        return self.ans

