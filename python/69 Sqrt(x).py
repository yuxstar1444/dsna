#brute force, test between 1 and x, test 1^2 , 2^2 ...etc
#use binary search, search space between 0 and x

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l<=r:
            m = 1 + ((r-l)//2)
            if m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
                res = m
            else:
                return m
        return res 
        
