class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        lenth = len(nums)
        if lenth==0:
            return nums
        i = 0
        j = lenth-1
        while i !=j and i<=j:
            if nums[i]%2 == 0 and nums[j]%2 ==1:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
            if nums[i]%2 != 0:
                i = i+1
            if nums[j]%2 == 0:
                j = j-1

        return nums
