class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here

        lenth = len(nums)
        sum = [0] * lenth
        sum[0] = nums[0]
        for i in range(1, lenth):
            sum[i] = max(nums[i] + sum[i - 1], nums[i])
        return max(sum)

