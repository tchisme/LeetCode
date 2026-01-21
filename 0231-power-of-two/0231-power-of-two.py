class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        
        for i in range(0,33,1):
            y = 2 ** i
            if n == y:
                return True
        return False

        