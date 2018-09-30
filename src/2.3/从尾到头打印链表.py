# 输入一个链表的头节点，从尾到头反过来打印出每个节点的值
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def printlistReverse(head):
    p = head
    stack = []
    while p.next != None:
        stack.append(p.val())

    while stack:
        print(stack[-1])
        stack.pop()