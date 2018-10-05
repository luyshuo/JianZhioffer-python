class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    # 将数组排序 ，找出copy中的min，定位在原数组的位置，即为min的逆数对个数 ，
    # 在原数组中把对应位置删除
    # 超时
    def reversePairs(self, A):
        # write your code here
        count = 0
        copy = []
        for i in A:
            copy.append(i)
        copy.sort()
        for i in range(len(copy)):
            count += A.index(copy[i])
            A.remove(copy[i])
        return count


