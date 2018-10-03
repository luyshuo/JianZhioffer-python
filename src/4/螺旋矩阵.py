class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    # 网上看到大佬的思路，通过列表反转 很强 不需要四次循环
    def spiralOrder(self, matrix):
        # write your code here
        llist = []
        try:
            while True:
                llist += matrix.pop(0)
                for i in matrix:
                    llist.append(i.pop())
                llist += matrix.pop()[::-1]
                for j in matrix[::-1]:
                    llist.append(j.pop(0))
        except:
            return llist


