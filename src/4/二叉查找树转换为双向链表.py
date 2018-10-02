"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def bstToDoublyList(self, root):
        # write your code here
        if not root:
            return None
        else:
            self.bstToDoublyList(root.left)
            if self.head == None:
                self.head = DoublyListNode(root.val)
                self.tail = self.head
            else:
                proot = DoublyListNode(root.val)
                self.tail.next = proot
                proot.prev = self.tail
                self.tail = proot

            self.bstToDoublyList(root.right)
            return self.head

