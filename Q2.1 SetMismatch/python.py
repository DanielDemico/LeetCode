class Solution(object):
    def findErrorNums(self, nums):
        
        list_ = []
        repet_num = None
        for i in nums:
            if nums.count(i) > 1:
                repet_num = i
                list_.append(repet_num)
                break

        for c, num in enumerate(nums):
            if c+1 not in nums:
                list_.append(c+1)
                
        return list_
