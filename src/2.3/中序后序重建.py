"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if len(inorder)==0:
            return None
        else:
            root = TreeNode(postorder[-1])
            i = inorder.index(root.val)
            root.left = self.buildTree(inorder[:i],postorder[:i])
            root.right = self.buildTree(inorder[i+1:],postorder[i:-1])
            return root
