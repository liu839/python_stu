class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x
        while i <= j:
            mid = (i+j)//2
            if mid**2 <= x and (mid+1)**2 > x:
                return mid
            else:
                if mid**2 < x:
                    i = mid+1
                elif mid**2 > x:
                    j = mid-1