class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        list_ = [0] *len(nums)
        
        for c, i in enumerate(nums):
            for j in range(len(nums)):
                if j == c:
                    pass
                elif nums[c] > nums[j]:
                    list_[c] +=1
        return list_
        