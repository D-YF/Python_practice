from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if root==None:
                return 0

            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)
            if leftHeight==-1 or rightHeight==-1 or abs(leftHeight-rightHeight)>1:
                return -1
            
            return max(leftHeight,rightHeight)+1
        
        ans = getHeight(root)
        return False if ans==-1 else True

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def getPath(node, path):
            path += str(node.val)

            if node.left==None and node.right==None:
                ans.append(path)
                return None
            
            if node.left:
                getPath(node.left,  path + '->')
            
            if node.right:
                getPath(node.right, path + '->')
            
            return None
        
        if root==None:
            return []
        getPath(root, '')

        return ans


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        
        leftValue = self.sumOfLeftLeaves(root.left)

        if root.left and root.left.left==None and root.left.right==None:
            leftValue = root.left.val

        rightValue = self.sumOfLeftLeaves(root.right)

        return leftValue + rightValue


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root==None: return None

        from collections import deque
        queue = deque()

        queue.append(root)
        ans = None

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                if i==0:
                    ans = cur.val

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return ans
            