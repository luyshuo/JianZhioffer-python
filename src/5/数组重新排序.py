class Solution:
    """
    @param nums: n non-negative integer array
    @return: A string
    """

    def minNumber(self, nums):
        # write your code here
        lst = list(map(str, nums))
        m = len(max(lst, key=len))
        newList = [(i, i + i[-1] * (m - len(i))) for i in lst]
        newList.sort(key=lambda item: item[1])
        result = ''.join((item[0] for item in newList))
        return str(int(result))
