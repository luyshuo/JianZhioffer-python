"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def __init__(self):
        self.r = []
        self.route = []

    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
        else:
            self.r.append(root.val)
            target -= root.val
            if target == 0 and root.left == None and root.right == None:
                self.route.append(list(self.r))
            self.binaryTreePathSum(root.left, target)
            self.binaryTreePathSum(root.right, target)

            self.r.pop()
            return self.route

