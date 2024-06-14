class Solution(object):
    def sortColors(self, nums):
        if len(nums) ==1:return
        countNum = [0,0,0]
        for x in nums:
            countNum[x]+=1
        idx = 0
        for x in range(len(countNum)):
            for y in range(countNum[x]):
                nums[idx]=x
                idx+=1
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        