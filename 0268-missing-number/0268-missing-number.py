class Solution(object):
    def missingNumber(self, nums):
        
         n = len(nums)
         true_sum = (n * (n + 1)) //2

         fake_sum = sum(nums)

         ans = true_sum - fake_sum
         return ans  
