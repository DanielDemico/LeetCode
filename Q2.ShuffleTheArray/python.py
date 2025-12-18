class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        lista = []
        for i in range(n):
            lista.append(nums[i])
            lista.append(nums[i + n])
        return lista