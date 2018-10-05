class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        res = [-1, -1]
        if A == None or len(A) == 0:
            return res
        res[0] = self.BoundaryLeft(A, 0, len(A) - 1, target)
        res[1] = self.BoundaryRight(A, 0, len(A) - 1, target)
        return res

    def BoundaryLeft(self, A, left, right, target):
        if A[0] == target:
            return 0
        while left <= right:
            median = (left + right) // 2
            if A[median] < target:
                left = median + 1
            elif A[median] > target:
                right = median - 1
            elif A[median] == target:
                if A[median - 1] != target:
                    return median
                else:
                    right = median - 1
        return -1

    def BoundaryRight(self, A, left, right, target):
        if A[right] == target:
            return right
        while left <= right:
            median = (left + right) // 2
            if A[median] < target:
                left = median + 1
            elif A[median] > target:
                right = median - 1
            elif A[median] == target:
                if A[median + 1] != target:
                    return median
                else:
                    left = median + 1
        return -1

