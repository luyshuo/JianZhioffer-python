"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        save = head
        while head != None:
            clonenode = RandomListNode(head.label)
            clonenode.next = head.next
            head.next = clonenode
            head = clonenode.next

        head = save
        while head != None:
            if head.random != None:
                head.next.random = head.random.next
            else:
                head.next.random = None
            head = head.next.next

        head = save.next
        while head:
            if head.next == None:
                head.next = None
                break
            else:
                head.next = head.next.next
                head = head.next
        return save.next
