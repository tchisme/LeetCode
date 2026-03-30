class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        max_value = max(nums)
        min_value = min(nums)

        ans = gcd(min_value,max_value)
        return ans
        