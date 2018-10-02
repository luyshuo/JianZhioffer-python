class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here
        al = [i for i in A]
        bl = [j for j in B]
        al.sort()
        bl.sort()
        if al == bl:
            return True
        else:
            return False
