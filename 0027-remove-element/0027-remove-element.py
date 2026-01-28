class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(0, len(nums)):
            if nums[i] != int(val):
                nums[index] = nums[i]
                index += 1
        
        return index
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        new = []

        for i in nums:
            if i != int(val):
                new.append(i)

        new.sort()
        
        return new
            