class Solution(object):
    def twoSum(self, nums, target):
        head = 0
        tail = 1
        while True:
            if tail >= len(nums):
                head += 1
                tail = head+1 
            if nums[head] + nums[tail] == target:
                return [head, tail]   
            tail += 1