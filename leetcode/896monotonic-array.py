class Solution:
    def isMonotonic(self,A: List[int]) -> bool:
        lens = len(A)
        if lens == 1:
            return True
        if lens == 0:
            return False
        flag = 1 if A[-1]>A[0] else -1
        for  i in range(1,lens):
            if A[i]*flag < A[i-1]*flag:
                return False
        return True