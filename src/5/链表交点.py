"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        # write your code here
        if headB and headA:
            p = p1 = headA
            ql = pl = 0
            q = q1 = headB
            while p:
                pl += 1
                p = p.next
            while q:
                ql += 1
                q = q.next
            if pl > ql:
                for i in range(pl - ql):
                    p1 = p1.next

            elif pl < ql:
                for i in range(ql - pl):
                    q1 = q1.next
            flag = 0
            while p1 and q1:
                if p1.val == q1.val and p1.next == q1.next:
                    return p1
                    break
                else:
                    p1 = p1.next
                    q1 = q1.next
            return None
        else:
            return None

