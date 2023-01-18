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


from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()

        if root==None:
            return []
        
        queue.append(root)
        while queue:
            size = len(queue)
            temp = []

            for i in range(size):
                cur = queue.popleft()
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(temp)
        
        return ans

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def bfs(root, depth):
            if root==None:
                return []
            
            if depth==len(ans): ans.append([])
            ans[depth].append(root.val)
            
            bfs(root.left,  depth+1)
            bfs(root.right, depth+1)
        bfs(root, 0)
        return ans

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()

        if root==None:
            return []
        queue.append(root)
        while queue:
            size = len(queue)
            temp = []

            for i in range(size):
                cur = queue.popleft()
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(temp)

        return ans[::-1]

#199
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque()

        if root==None:
            return []
        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
            ans.append(cur.val)
        return ans

# 637
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            size = len(queue)
            sum = 0

            for i in range(size):
                cur = queue.popleft()
                sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            ans.append(sum/size)
        return ans


# 429
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            temp = []
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                temp.append(cur.val)

                for child in cur.children:
                    queue.append(child)
            ans.append(temp)
        return ans
