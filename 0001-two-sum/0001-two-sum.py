class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        NumsMap = {}

        for i in range(n):
            complement = target - nums[i]
            if complement in NumsMap:
                return [NumsMap[complement] , i]
            NumsMap[nums[i]] = i
        
        return []

       

        