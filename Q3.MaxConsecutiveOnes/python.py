class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c = 0
        c_aux = 0
        for i in nums:
            if i == 1:
                c+=1
            else:
                c=0
            c_aux = c if c > c_aux else c_aux
        return c_aux
        