# 515.在每个树行中找最大值
# 116.填充每个节点的下一个右侧节点指针
# 117.填充每个节点的下一个右侧节点指针II
# 104.二叉树的最大深度
# 111.二叉树的最小深度

from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque()

        if root:
            queue.append(root)
        
        while queue:
            size = len(queue)
            temp = []

            for i in range(size):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(max(temp))
        return ans




# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                if i<size-1:
                    cur.next = queue[0]
        
        return root




class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxD(root):
            if root==None:
                return 0
            
            max_left = maxD(root.left)
            max_right = maxD(root.right)
            return max(max_left, max_right)+1

        return maxD(root)

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def minD(root):
            if root==None:
                return 0
            
            if root.left == None:
                return minD(root.right)+1
            elif root.right == None:
                return minD(root.left)+1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right))+1
        
        return minD(root)