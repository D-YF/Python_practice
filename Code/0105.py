class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0]*n for _ in range(n)]
        loop = n//2 # the number of circles
        startx, starty = 0, 0
        value = 1

        for offset in range(1, loop+1):
            for i in range(starty, n-offset):
                result[startx][i] = value
                value += 1
            
            for i in range(startx, n-offset):
                result[i][n-offset] = value
                value += 1

            for i in range(n-offset, starty, -1):
                result[n-offset][i] = value
                value += 1

            for i in range(n-offset, startx, -1):
                result[i][starty] = value
                value += 1

            startx += 1
            starty += 1
        
        if n%2 == 1:
            result[loop][loop] = value
        return result

n = 1
sol = Solution()
print(sol.generateMatrix(n))

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(next=head)
        cur = new_head

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return new_head.next
        
# head = [], val = 1

class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self.size:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        NewNode = Node(val)
        NewNode.next = self.head.next
        self.head.next = NewNode
        self.size += 1
        return None

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur = self.head
        tail = Node(val)
        while cur.next:
            cur = cur.next
        
        cur.next = tail
        self.size += 1
        return None

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index==0:
            self.addAtHead(val)
            return
        elif index==self.size:
            self.addAtTail(val)
            return
        elif index>self.size:
            return
        
        NewNode = Node(val)
        cur = self.head.next
        for i in range(index-1):
            cur = cur.next
        NewNode.next = cur.next
        cur.next = NewNode
        self.size += 1
        return None


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        # Not head.next (might delete index=0)
        cur = self.head

        if index<0 or index >= self.size:
            return None

        for i in range(index):
            cur = cur.next

        cur.next = cur.next.next
        self.size -= 1
        return None


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
print(obj.get(6))
obj.deleteAtIndex(0)
print(obj.get(0))