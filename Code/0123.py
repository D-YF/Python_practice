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


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def search(root):
            if root==None: return None

            if key==root.val:
                if root.left==None and root.right==None:
                    return None
                elif root.left==None and root.right:
                    root = root.right
                elif root.right==None and root.left:
                    root = root.left
                else:
                    left = root.left
                    root = root.right
                    cur = root
                    while cur.left:
                        cur = cur.left
                    cur.left = left
            elif key>root.val:
                root.right = search(root.right)
            else:
                root.left = search(root.left)
            return root
        
        return search(root)
    

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(root):
            if root==None:
                return None
            
            if low<=root.val<=high:
                root.left = trim(root.left)
                root.right = trim(root.right)
            elif root.val<low:
                root = trim(root.right)
            elif root.val>high:
                root = trim(root.left)
            return root

        return trim(root)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def buildTree(nums):
            N = len(nums)
            if N==0: return None

            mid = N//2
            root = TreeNode(val=nums[mid])
            root.left = buildTree(nums[:mid])
            root.right = buildTree(nums[mid+1:])
            return root
        
        return buildTree(nums)


class Solution:
    def __init__(self) -> None:
        self.pre = None

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def antiSearch(root):
            if root==None:
                return None
            cur = root

            cur.right = antiSearch(root.right)

            if self.pre:
                cur.val += self.pre.val
            self.pre = cur

            cur.left = antiSearch(root.left)
            return cur

        return antiSearch(root)