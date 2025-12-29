class Solution(object):
    def findDisappearedNumbers(self, nums):
        for n in nums:
            idx = abs(n) -1
            nums[idx] = -abs(nums[idx])
        
        l = []
        for i, v in enumerate(nums):
            if v > 0:
                l.append(i + 1)
        return l    
        
        

    