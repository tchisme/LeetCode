class Solution(object):
    def nextGreatestLetter(self, letters, target):
        
        x = ord(target)
        for i in letters:
            if ord(i) > x:
                return i
        
        return letters[0]
       
        

        